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

```

### GPU/CPU Configuration

For TensorFlow-based calculations, you can specify GPU or CPU usage following [these instructions](https://stackoverflow.com/questions/40069883/how-to-set-specific-gpu-in-tensorflow).

---

### Git Large File Storage (LFS)

This repository uses Git LFS to handle large files. Ensure Git LFS is installed on your system by following the instructions on the [Git LFS website](https://git-lfs.github.com/).

Once installed, clone the repository as usual with `git clone` — large files will be downloaded automatically. If you've already cloned without Git LFS, retrieve the large files with:

```console
git lfs pull
```
