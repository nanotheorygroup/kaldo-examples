# Compute Thermal Conductivity of Silicon with pheasy-Extracted Force Constants

> [pheasy](https://gitlab.com/cplin/pheasy) fits interatomic force constants from a compact set of symmetry-reduced, randomly displaced supercells and DFT (or ML potential) forces. See the pheasy repository and paper ([arXiv:2508.01020](https://arxiv.org/abs/2508.01020)) for the full method.

> **Installing pheasy**: install from the GitLab source (`git clone https://gitlab.com/cplin/pheasy.git && pip install -e ./pheasy`). The package on PyPI is outdated (0.0.2) and does not match the current code or this workflow.

1. Generate the symmetry-irreducible force constant clusters (null space) and the randomly displaced supercells with pheasy:

```console
pheasy -s -c --dim 3 3 3 --pcell POSCAR
pheasy -d -n <N> --dim 3 3 3 --pcell POSCAR
```

`<N>` is the number of displaced supercells pheasy determines are needed from the crystal symmetry. Quantum ESPRESSO users add `--qe --pcell cell.in` to both commands so the generated supercells are written in QE input format. See the pheasy repository for the full set of flags and displacement conventions.

2. Compute forces for each displaced supercell with your DFT code of choice. VASP users collect `vasprun.xml.001` through `vasprun.xml.<N>`; QE users collect `DISP.out.001` through `DISP.out.<N>`.

3. Fit the force constants with pheasy:

```console
pheasy -f -n <N> --dim 3 3 3 --pcell POSCAR
```

This produces `FORCE_CONSTANTS` (2nd order, phonopy-style text, eV/A^2) and `FORCE_CONSTANTS_3RD` (3rd order, ShengBTE-style text, eV/A^3). For polar materials, add `--nac` together with a `born.fmt` file (Born effective charges and the dielectric tensor) to fit with the non-analytic correction; kaldo reads `born.fmt` directly for the NAC as well.

4. Run kaldo directly on the pheasy working directory with `format='pheasy'`:

```console
cd density_functional_theory/silicon_dft_pheasy/
python thermal_conductivity.py
```

After finishing this step, you can run the Jupyter notebook `phonons_and_conductivity.ipynb` to plot the phonon dispersion and print the conductivity.

**kaldo version requirement**: this example needs a kaldo build with `format='pheasy'` support, currently on [nanotheorygroup/kaldo PR #286](https://github.com/nanotheorygroup/kaldo/pull/286), until it is merged and released.

## Data provenance

The files in `fc_pheasy/` (`POSCAR`, `FORCE_CONSTANTS`, `FORCE_CONSTANTS_3RD`) are silicon force constants derived from kaldo's own hiphive-fitted reference for silicon, rewritten in pheasy's exact output conventions. No pheasy-produced (GPL-distributed) data is used. A real pheasy workflow produces these same files by running pheasy on DFT forces, following the four steps above.

Reference thermal conductivity for this example (3x3x3 2nd and 3rd order supercell, 7x7x7 k-point mesh):
- **289.2 W/m-K (Inversion), 256.6 W/m-K (RTA)**
