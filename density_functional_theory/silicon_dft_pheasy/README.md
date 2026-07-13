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

The files in `fc_pheasy/` (`POSCAR`, `FORCE_CONSTANTS`, `FORCE_CONSTANTS_3RD`) are genuine force constants fitted by pheasy from Quantum ESPRESSO DFT forces. In short: 12 symmetry-reduced randomly-displaced 3x3x3 supercells (54 atoms), forces from `pw.x` (PBE, PAW pseudopotential, ecutwfc 60 Ry, ecutrho 480 Ry, 3x3x3 k-mesh, 1e-10 SCF threshold), fit with pheasy (`--dim 3 3 3`, 3rd-order cutoff at the 3rd nearest neighbor, least-squares RMSE 4e-5 eV/A). The exact recipe is in "How the shipped force constants were computed" below. Only the resulting `FORCE_CONSTANTS`/`FORCE_CONSTANTS_3RD` text outputs are shipped; no pheasy-produced (GPL-distributed) intermediate data is redistributed.

Reference thermal conductivity for this example (3x3x3 2nd and 3rd order supercell, 7x7x7 k-point mesh):
- **128.0 W/m-K (Inversion), 123.4 W/m-K (RTA)**

These values sit close to the experimental room-temperature conductivity of silicon (about 130-150 W/m-K). A fit with more displaced configurations or a shorter third-order cutoff will shift them; the point of the example is the pheasy-to-kaldo workflow, not a converged production number.

## How the shipped force constants were computed

The `fc_pheasy/` files were produced with Quantum ESPRESSO (`pw.x`) and pheasy as follows.

**1. Primitive cell** (`Si.in`), a relaxed 2-atom FCC silicon cell (a = 5.4692 A):

```
 &CONTROL
    calculation = "scf", tprnfor = .TRUE., prefix = "Si",
    outdir = "./out/", pseudo_dir = "./pseudo",
 /
 &SYSTEM
    ibrav = 0, nat = 2, ntyp = 1,
    ecutwfc = 60, ecutrho = 480, occupations = "fixed",
 /
 &ELECTRONS
    conv_thr = 1.0D-10,
 /
ATOMIC_SPECIES
    Si   28.0855   Si.pbe-n-kjpaw_psl.1.0.0.UPF
K_POINTS automatic
  8 8 8   0 0 0
CELL_PARAMETERS (angstrom)
   0.000000000   2.734600522   2.734600522
   2.734600522   0.000000000   2.734600522
   2.734600522   2.734600522   0.000000000
ATOMIC_POSITIONS (crystal)
Si   0.00   0.00   0.00
Si   0.25   0.25   0.25
```

The PAW pseudopotential is `Si.pbe-n-kjpaw_psl.1.0.0.UPF` from [PSlibrary](https://www.quantum-espresso.org/pseudopotentials/). The example loads this cell as the `POSCAR` in `fc_pheasy/`.

**2. Generate displaced supercells** with pheasy in QE format (writes `DISP.in.001` ... `DISP.in.012`):

```console
pheasy -s -c --dim 3 3 3 --qe --pcell Si.in
pheasy -d -n 12 --dim 3 3 3 --qe --pcell Si.in
```

The 3x3x3 supercells inherit the primitive electronic settings (ecutwfc 60, ecutrho 480, conv_thr 1e-10) at a 3x3x3 k-mesh (54 atoms per supercell).

**3. Compute forces** by running `pw.x` on each displaced input:

```console
for i in $(seq -w 1 12); do
    mpirun -np <ncores> pw.x -inp DISP.in.$i > DISP.out.$i
done
```

**4. Fit 2nd and 3rd order force constants** (least-squares, RMSE 4e-5 eV/A):

```console
pheasy -f -n 12 -w 3 --c3 -3 --dim 3 3 3 --qe --pcell Si.in
```

`-w 3` includes up to third order and `--c3 -3` sets the third-order cutoff at the 3rd nearest neighbor. This writes the `FORCE_CONSTANTS` and `FORCE_CONSTANTS_3RD` shipped in `fc_pheasy/`.
