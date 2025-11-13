# `carbon_diamond_Tersoff_ASE_LAMMPS`

Example carbon_diamond_Tersoff_ASE_LAMMPS illustrates how to perform thermal transport simulation for a carbon 
diamond (2 atoms per cell) system using [ASE and LAMMPS](https://wiki.fysik.dtu.dk/ase/_modules/ase/calculators/lammpslib.html) as force calculator.

External files required: 
		       1). forcefields/C.tersoff

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

			      
-   `carbon_diamond_Tersoff_thermal_conductivity.py` proceeds as follows:

    1. Set up force constant object and compute 2nd, 3rd force constants using C.tersoff.

    2. Set up phonon object (15x15x15 k-point mesh) and perform quantum simulation at 300K.

    3. Set up Conductivity object and compute thermal conductivity with Relaxation Time Approximation (RTA), 
				self-consistent (sc) and direct inversion of scattering matrix (inverse) methods.
   
    4. Visualize intermediate quantities during the thermal transport simulations.


- To run this example, navigate to this directory and execute:

```console
python carbon_diamond_Tersoff_thermal_conductivity.py
```
- To view figures generated during simulations, navigate to this folder: ***plots/15_15_15/***
- To access data computed during simulations, navigate to this folder: ***ALD_c_diamond***

- Reference conductivity (5x5x5 supercell,15x15x15 k-point mesh, inverse):  2512.3 W/m-K (Quantum) 
