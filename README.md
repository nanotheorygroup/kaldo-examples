# kALDo Examples

Official repository demonstrating various examples to use [kALDo](https://github.com/nanotheorygroup/kaldo) for thermal transport calculations.

<p align="center">
<img src="kaldo-schema.png" width="450">
</p>

## Overview

This repository provides examples demonstrating how to compute thermal conductivity using kALDo with two complementary approaches:

- **Boltzmann Transport Equation (BTE)**: Solves for phonon populations under a temperature gradient
- **Quasi-Harmonic Green-Kubo (QHGK)**: A unified approach interpolating between particle-like and wave-like thermal transport

The examples cover workflows with:

- **Machine Learning Potentials** (orb, NEP, MatterSim, ACE, UPET)
- **Density Functional Theory** (Quantum ESPRESSO, D3Q)
- **Empirical Potentials** (Any Empirical Potentials Supported in LAMMPS)
- **Finite Temperature Effective Potentials** (TDEP)

## Contributing

We welcome contributions from the community! If you have a thermal transport workflow using kALDo — whether with a new potential, a different material system, or an alternative method — we'd love to include it.

### How to contribute an example

1. Fork the repository and create a new branch (`git checkout -b your-branch-name`)
2. Add your example in the appropriate category folder (`machine_learning_potentials/`, `density_functional_theory/`, or `empirical_potentials/`)
3. Include a `README.md` describing the calculation and a Jupyter notebook (`.ipynb`) for visualization
4. Push your branch and open a Pull Request

The documentation is auto-generated from the example folders, so your example will automatically appear on the docs site once merged.

For questions or suggestions, feel free to [open an issue](https://github.com/nanotheorygroup/kaldo-examples/issues).

## Building the Documentation

### Requirements

```bash
pip install sphinx sphinx-immaterial nbsphinx myst-parser
```

### Build

```bash
cd docs
make html
```

The documentation will be generated in `docs/_build/html/`.
