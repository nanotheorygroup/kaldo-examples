# empirical_potentials
This collection of examples shows how to perform thermal transport with kALDo for cystal and amorphous
systems using [Tersoff potential](https://docs.lammps.org/pair_tersoff.html). Before running simulations with kALDo, download the following third-party packages: [LAMMPS](https://lammps.sandia.gov/download.html)
- To calculate 2<sup>nd</sup> and 3<sup>rd</sup> order force constants with LAMMPS and ASE, after downloading [LAMMPS](https://lammps.sandia.gov/),compile LAMMPS with shlib mode:
```console
cd path/to/lammps/src
make yes-manybody
make yes-molecule
make mpi mode=shlib
```
- After properly install kALDo, run the following line in command window to link LAMMPS with Python and ASE:
```console
cd path/to/lammps/src
make install-python				
```
- In amorphous silicon and silicon clathrate examples, 2<sup>nd</sup> and 3<sup>rd</sup> order force constants are computed by using LAMMPS PHONON package. Since these material systems have relatively large  unit cell, computing force constants using the PHONON package currently available in the official website can take hours. 
To speed up the calculation, one can download and compile LAMMPS with optimized force constants calculation functionality from the following repo: [OptimizedDynamicalMatrix](https://github.com/charlessievers/lammps/tree/fed47b9ffc833bebffe0e460739ebd6ff69e9c8d). 
- Some features on the OptimizedDynamicalMatrix are broken as of commits in April 2020, please checkout the following commit which works reliably from 01/29/2020:
        - in your cloned repo: `git checkout fed47b9ffc833bebffe0e460739ebd6ff69e9c8d`
- To obtain precalculated force constants for each example, navigate to each example folder and execute:
```console
chmod +x get_precalculated_fc.sh
./get_precalculated.sh
```
- To obtain reference calculations of phonon properties and plots for each example, navigate to each example folder and execute:
```console
chmod +x get_reference.sh
./get_reference.sh
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
