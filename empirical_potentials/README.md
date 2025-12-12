# Empirical Potentials

These examples demonstrate kALDo workflows using **empirical interatomic potentials**. Classical potentials like Tersoff and Stillinger-Weber provide computationally efficient force evaluations, enabling thermal transport calculations for large systems and complex structures. The workflows shown here use **LAMMPS** and **ASE** for force constant calculations.

---

## Setup Instructions

This collection shows how to perform thermal transport with kALDo for crystal and amorphous systems using the [Tersoff potential](https://docs.lammps.org/pair_tersoff.html).

### Requirements

Download and install [LAMMPS](https://lammps.sandia.gov/download.html) before running these examples.

### Compiling LAMMPS with ASE support

To calculate 2nd and 3rd order force constants with LAMMPS and ASE, compile LAMMPS with shlib mode:

```console
cd path/to/lammps/src
make yes-manybody
make yes-molecule
make mpi mode=shlib
```

Then link LAMMPS with Python and ASE:

```console
cd path/to/lammps/src
make install-python
```

### Optimized force constants for large systems

For amorphous silicon and silicon clathrate examples, force constants are computed using the LAMMPS PHONON package. For large unit cells, this can take hours. To speed up calculations, use the optimized version from [OptimizedDynamicalMatrix](https://github.com/charlessievers/lammps/tree/fed47b9ffc833bebffe0e460739ebd6ff69e9c8d).

**Note:** Use commit `fed47b9ffc833bebffe0e460739ebd6ff69e9c8d` for reliable results:

```console
git checkout fed47b9ffc833bebffe0e460739ebd6ff69e9c8d
```
