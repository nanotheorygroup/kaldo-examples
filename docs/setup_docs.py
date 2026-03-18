#!/usr/bin/env python3
"""Set up documentation structure - use README.md and ipynb files directly."""

import re
import shutil
from pathlib import Path

# Use script location to determine paths (works on any system)
DOCS_ROOT = Path(__file__).parent.resolve()
REPO_ROOT = DOCS_ROOT.parent
DOCSOURCE = DOCS_ROOT / "docsource"

CATEGORIES = {
    "machine_learning_potentials": "Machine Learning Potentials",
    "density_functional_theory": "Density Functional Theory",
    "empirical_potentials": "Empirical Potentials"
}

def get_title_from_folder(folder_name):
    """Convert folder name to readable title."""
    name = re.sub(r'^\d+[-_]', '', folder_name)
    return name.replace("_", " ").replace("-", " ").title()

def find_all_notebooks(example_dir):
    """Find all notebooks in an example directory (including subdirs), sorted by path."""
    notebooks = []

    # Root level notebooks
    notebooks.extend(sorted(example_dir.glob("*.ipynb")))

    # Subdirectory notebooks (sorted by subdirectory name for correct order)
    for sub_dir in sorted(example_dir.iterdir()):
        if not sub_dir.is_dir() or sub_dir.name.startswith('.'):
            continue
        notebooks.extend(sorted(sub_dir.glob("*.ipynb")))
        # Check nested dirs (like silicon_NEP89_calorine/NEP-Si-expert)
        for nested_dir in sorted(sub_dir.iterdir()):
            if nested_dir.is_dir() and not nested_dir.name.startswith('.'):
                notebooks.extend(sorted(nested_dir.glob("*.ipynb")))

    return notebooks


def prepare_notebook_for_docs(nb_path, title):
    """Prepare a copied notebook for documentation: add title and fix headings."""
    import json
    with open(nb_path, 'r') as f:
        nb = json.load(f)

    # Create title cell
    title_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [f"# {title}"]
    }

    # Insert title at beginning
    nb['cells'].insert(0, title_cell)

    # Downgrade all headings by 2 levels (# -> ###, ## -> ####) in other cells
    # This prevents internal headings from appearing in the TOC
    for cell in nb['cells'][1:]:  # Skip the title cell we just added
        if cell.get('cell_type') == 'markdown':
            source = cell.get('source', [])
            if isinstance(source, list):
                new_source = []
                for line in source:
                    # Downgrade headings: add ## to any line starting with #
                    if line.lstrip().startswith('#'):
                        leading_space = len(line) - len(line.lstrip())
                        new_source.append(' ' * leading_space + '##' + line.lstrip())
                    else:
                        new_source.append(line)
                cell['source'] = new_source
            elif isinstance(source, str):
                lines = source.split('\n')
                new_lines = []
                for line in lines:
                    if line.lstrip().startswith('#'):
                        leading_space = len(line) - len(line.lstrip())
                        new_lines.append(' ' * leading_space + '##' + line.lstrip())
                    else:
                        new_lines.append(line)
                cell['source'] = '\n'.join(new_lines)

    with open(nb_path, 'w') as f:
        json.dump(nb, f, indent=1)

def merge_notebooks(notebook_paths):
    """Merge multiple notebooks into one, returning the combined notebook dict."""
    import json

    if not notebook_paths:
        return None

    # Start with the first notebook as base
    with open(notebook_paths[0], 'r') as f:
        merged = json.load(f)

    # Append cells from remaining notebooks
    for nb_path in notebook_paths[1:]:
        with open(nb_path, 'r') as f:
            nb = json.load(f)
        # Add a separator between notebooks
        separator = {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["---"]
        }
        merged['cells'].append(separator)
        merged['cells'].extend(nb.get('cells', []))

    return merged

def process_examples(category):
    """Process examples - merge notebooks and/or copy README, return list of doc paths."""
    import json
    cat_path = REPO_ROOT / category
    dest_dir = DOCSOURCE / category
    dest_dir.mkdir(parents=True, exist_ok=True)

    examples = []

    for example_dir in sorted(cat_path.iterdir()):
        if not example_dir.is_dir() or example_dir.name.startswith('.'):
            continue

        example_name = example_dir.name
        title = get_title_from_folder(example_name)
        readme = example_dir / "README.md"
        notebooks = find_all_notebooks(example_dir)

        # Prefer notebooks if available, otherwise use README
        if notebooks:
            dest_path = dest_dir / f"{example_name}.ipynb"
            if len(notebooks) == 1:
                shutil.copy2(notebooks[0], dest_path)
                print(f"Copied: {notebooks[0].name} -> {dest_path.name}")
            else:
                # Merge multiple notebooks
                merged = merge_notebooks(notebooks)
                with open(dest_path, 'w') as f:
                    json.dump(merged, f, indent=1)
                print(f"Merged {len(notebooks)} notebooks -> {dest_path.name}")
            # Prepare notebook for docs (add title, fix headings)
            prepare_notebook_for_docs(dest_path, title)
            examples.append(example_name)
        elif readme.exists():
            dest_path = dest_dir / f"{example_name}.md"
            shutil.copy2(readme, dest_path)
            print(f"Copied: {readme.name} -> {dest_path.name}")
            examples.append(example_name)

    return examples

def read_category_content(category):
    """Read category README and return (intro, details) tuple.

    intro: First paragraph after title (for before toctree)
    details: Everything else (for after toctree)
    """
    readme_path = REPO_ROOT / category / "README.md"
    if readme_path.exists():
        content = readme_path.read_text().strip()
        lines = content.split('\n')

        # Skip the first heading
        if lines and lines[0].startswith('#'):
            lines = lines[1:]

        content = '\n'.join(lines).strip()

        # Split on first "---" separator
        if '\n---\n' in content:
            parts = content.split('\n---\n', 1)
            intro = parts[0].strip()
            details = parts[1].strip() if len(parts) > 1 else ""
            return intro, details

        return content, ""
    return "", ""

def generate_category_index(category, category_title, examples, intro, details):
    """Generate an index.rst for a single category."""
    dest_dir = DOCSOURCE / category

    # Build RST underline (must be at least as long as the title)
    underline = '=' * len(category_title)

    content = f'''{category_title}
{underline}

{intro}

.. toctree::
   :maxdepth: 1

'''

    for example_name in examples:
        title = get_title_from_folder(example_name)
        content += f"   {title} <{example_name}>\n"

    if details:
        content += f"\n\n.. include:: ../../../{category}/README_details.md\n   :parser: myst_parser.sphinx_\n"

    index_path = dest_dir / "index.rst"
    index_path.write_text(content)
    print(f"Generated: {index_path}")


def generate_main_index(examples_by_category):
    """Generate the main index.rst file."""

    # Read category content (intro + details)
    category_content = {}
    for category in CATEGORIES:
        intro, details = read_category_content(category)
        category_content[category] = (intro, details)

    # Generate category sub-index pages
    for category, cat_title in CATEGORIES.items():
        examples = examples_by_category.get(category, [])
        intro, details = category_content[category]
        generate_category_index(category, cat_title, examples, intro, details)

    # Generate main index referencing category sub-indexes
    content = '''.. kALDo Examples documentation

.. image:: docsource/_resources/logo.png
   :width: 400

Examples
========

Understanding thermal transport in materials is crucial for applications ranging from thermoelectrics to thermal management in electronics. **Anharmonic lattice dynamics** captures the phonon-phonon interactions that govern heat conduction beyond the harmonic approximation.

This repository provides examples demonstrating how to use `kALDo <https://github.com/nanotheorygroup/kaldo>`_ to compute thermal conductivity using two complementary approaches:

- **Boltzmann Transport Equation (BTE)**: Solves for phonon populations under a temperature gradient, capturing both normal and Umklapp scattering processes.
- **Quasi-Harmonic Green-Kubo (QHGK)**: A unified approach that interpolates between the particle-like (BTE) and wave-like (Allen-Feldman) pictures of thermal transport.

The examples cover workflows with machine learning potentials, density functional theory (DFT), and empirical potentials.


.. toctree::
   :maxdepth: 2

   docsource/machine_learning_potentials/index
   docsource/density_functional_theory/index
   docsource/empirical_potentials/index


Contributing
------------

We welcome contributions from the community! If you have a thermal transport workflow using kALDo — whether with a new potential, a different material system, or an alternative method — we'd love to include it.

**How to contribute an example:**

1. Fork the repository and create a new branch
2. Add your example in the appropriate category folder (``machine_learning_potentials/``, ``density_functional_theory/``, or ``empirical_potentials/``)
3. Include a ``README.md`` describing the calculation and a Jupyter notebook (``.ipynb``) for visualization
4. Push your branch and open a Pull Request

The documentation is auto-generated from the example folders, so your example will automatically appear on the docs site once merged.

For questions or suggestions, feel free to `open an issue <https://github.com/nanotheorygroup/kaldo-examples/issues>`_.
'''

    index_path = DOCS_ROOT / "index.rst"
    index_path.write_text(content)
    print(f"\nGenerated: {index_path}")

    # Write details files for include
    for category in CATEGORIES:
        _, details = category_content[category]
        if details:
            details_path = REPO_ROOT / category / "README_details.md"
            details_path.write_text(details)
            print(f"Generated: {details_path}")

def main():
    print("Setting up documentation...\n")

    examples_by_category = {}

    for category in CATEGORIES:
        cat_path = REPO_ROOT / category
        if not cat_path.exists():
            continue

        # Clean destination
        dest_cat = DOCSOURCE / category
        if dest_cat.exists():
            shutil.rmtree(dest_cat)
        dest_cat.mkdir(parents=True, exist_ok=True)

        # Process examples
        examples_by_category[category] = process_examples(category)

    generate_main_index(examples_by_category)
    print("\nDone! Run 'make html' in the docs directory to build.")

if __name__ == "__main__":
    main()
