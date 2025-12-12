# `silicon_clathrate_Tersoff_LAMMPS`

Example silicon_clathrate_Tersoff_LAMMPS illustrates how to perform thermal 
transport simulation for a type I clathrate (46 atoms per cell) system using
[LAMMPS PHONON ](https://docs.lammps.org/Packages_details.html#pkg-phonon) package as force calculator.

External files required: 
		       1). forcefields/Si.tersoff


- The force constant calculation proceeds as follows:

    in.Si46:
    1.  Compute 2nd, 3rd force constants computed with LAMMPS PHONON		

-   thermal_conductivity.py proceeds as follows:

    1. Set up force constant object by loading in computed 2nd, 3rd force constants computed with LAMMPS USER-PHONON.

    2. Set up phonon object (3x3x3 k-point mesh) and perform quantum simulation at 300K.

    3. Set up Conductivity object and compute thermal conductivity with Relaxation Time Approximation (RTA) method.


- To compute 2<sup>nd</sup> and 3<sup>rd</sup> order force constants with LAMMPS PHONON, navigate to this directory and execute:
```console
./mpirun -np 8 /path/to/lammps/src/lmp_mpi < in.Si46 > Si46.log 
```

- To view figures generated during simulations, navigate to this folder: ***plots/3_3_3/***
- To access data computed during simulations, navigate to this folder: ***ALD_Si_46***
- Warning: While computing force constants using LAMMPS with a triclinic (non-orthogonal) cell, it follows a strict right-handed cell convention. More information about the cell conventioncan be found [here](https://docs.lammps.org/Howto_triclinic.html). The unit cell of the structure used in this example has been made based on the right-handed cell convention. Please be aware of this rule if lammps inputs were prepared from scratch. Alternatively, it is welcome to refer our [carbon nanotube example](https://github.com/nanotheorygroup/kaldo/tree/main/examples/carbon_nanotube_Tersoff_LAMMPS) where we imposed this convention and prepared lammps input files via a python script.
 
