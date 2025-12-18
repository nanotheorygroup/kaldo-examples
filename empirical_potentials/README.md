# Empirical Potentials

These examples demonstrate kALDo workflows using **empirical interatomic potentials**. Classical potentials like Tersoff and Stillinger-Weber provide computationally efficient force evaluations, enabling thermal transport calculations for large systems and complex structures. The workflows shown here use **LAMMPS** and **ASE** for force constant calculations.

---

### Setup Instructions

These examples use the [Tersoff potential](https://docs.lammps.org/pair_tersoff.html) for interatomic interactions.

### Requirements

Download and install [LAMMPS](https://lammps.sandia.gov/download.html) before running these examples.

### Compiling LAMMPS with Python/ASE support

To calculate 2nd and 3rd order force constants with LAMMPS and ASE, compile LAMMPS with shared library support using cmake:

```console
cd path/to/lammps/src
mkdir build
cd build
cmake ../cmake -DLAMMPS_EXCEPTIONS=yes \
               -DBUILD_SHARED_LIBS=yes \
               -DMLIAP_ENABLE_PYTHON=yes \
               -DPKG_PYTHON=yes \
               -DPKG_MANYBODY=yes \
               -DPKG_KSPACE=yes \
               -DPKG_PHONON=yes \
               -DPYTHON_EXECUTABLE:FILEPATH=`which python`
make -j 16
make install-python
```

### GPU/CPU Configuration

For TensorFlow-based calculations, you can specify GPU or CPU usage following [these instructions](https://stackoverflow.com/questions/40069883/how-to-set-specific-gpu-in-tensorflow).

---
### List and content of examples folder
For each example, more detailed information is provided by the README.md file contained in the corresponding directory.
- `amorphous_silicon_Tersoff_LAMMPS:`
This example illustrates how to perform thermal transport simulation for an amorphous silicon system (512 atoms per cell) with [LAMMPS PHONON](https://docs.lammps.org/Packages_details.html#pkg-phonon) package as force calculator.
- `carbon_diamond_Tersoff_ASE_LAMMPS:`
This example illustrates how to perform thermal transport simulation for a carbon diamond (2 atoms per cell) system using [ASE and LAMMPS](https://wiki.fysik.dtu.dk/ase/_modules/ase/calculators/lammpslib.html) as force calculator.
- `carbon_nanotube_Tersoff_LAMMPS:`
This example illustrates how to perform thermal transport simulation for a 10,0 carbon nanotube (40 atoms per cell) system using [LAMMPS PHONON](https://docs.lammps.org/Packages_details.html#pkg-phonon) package as force calculator.
- `silicon_clathrate_Tersoff_LAMMPS:`
This example illustrates how to perform thermal transport simulation for a type I clathrate (46 atoms per cell) system using [LAMMPS PHONON](https://docs.lammps.org/Packages_details.html#pkg-phonon) package as force calculator.

---
### Git Large File Storage (LFS)

This repository uses Git LFS to handle large files. Ensure Git LFS is installed on your system by following the instructions on the [Git LFS website](https://git-lfs.github.com/).

Once installed, clone the repository as usual with `git clone` — large files will be downloaded automatically. If you've already cloned without Git LFS, retrieve the large files with:

```console
git lfs pull
```
