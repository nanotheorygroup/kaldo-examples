# empirical_potentials
This collection of examples shows how to perform thermal transport with kALDo for cystal and amorphous
systems using [Tersoff potential](https://docs.lammps.org/pair_tersoff.html). Before running simulations with kALDo, download the following third-party packages: [LAMMPS](https://lammps.sandia.gov/download.html)
- To calculate 2<sup>nd</sup> and 3<sup>rd</sup> order force constants with LAMMPS and ASE,compile LAMMPS with shlib mode using cmake:
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

- Suggestions of specificing GPU/CPU usage for tensorflow can be accessed [here](https://stackoverflow.com/questions/40069883/how-to-set-specific-gpu-in-tensorflow).

## List and content of examples folder
For each example, more detailed information is provided by the README.md file contained in the corresponding directory.
- `amorphous_silicon_Tersoff_LAMMPS:`
This example illustrates how to perform thermal transport simulation for an amorphous silicon system (512 atoms per cell) with [LAMMPS PHONON](https://docs.lammps.org/Packages_details.html#pkg-phonon) package as force calculator.
- `carbon_diamond_Tersoff_ASE_LAMMPS:`
This example illustrates how to perform thermal transport simulation for a carbon diamond (2 atoms per cell) system using [ASE and LAMMPS](https://wiki.fysik.dtu.dk/ase/_modules/ase/calculators/lammpslib.html) as force calculator.
- `carbon_nanotube_Tersoff_LAMMPS:`
This example illustrates how to perform thermal transport simulation for a 10,0 carbon nanotube (40 atoms per cell) system using [LAMMPS PHONON](https://docs.lammps.org/Packages_details.html#pkg-phonon) package as force calculator.
- `silicon_clathrate_Tersoff_LAMMPS:`
This example illustrates how to perform thermal transport simulation for a type I clathrate (46 atoms per cell) system using [LAMMPS PHONON](https://docs.lammps.org/Packages_details.html#pkg-phonon) package as force calculator.
