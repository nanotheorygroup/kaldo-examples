# `amorphous_silicon_Tersoff_LAMMPS`

Example amorphous_silicon_Tersoff_LAMMPS illustrates how to perform thermal 
transport simulation for an amorphous silicon sample (512 atoms system) with
[LAMMPS PHONON](https://docs.lammps.org/Packages_details.html#pkg-phonon) package as force calculator.

External files required: 
		       1). forcefields/Si.tersoff 
		       2). fc_aSi512/replicated_atoms.xyz: amorphous silicon structures (same structure as aSi_512.lmp).


- The force constants calculation proceeds as follows:
			
	in.aSi512:
    1.  Compute 2nd and 3rd force constants with LAMMPS PHONON
			
- thermal_conductivity.py proceeds as follows:

    1. Set up force constant object by loading in 2nd, 3rd force constants computed with LAMMPS PHONON.
			
	2. Set up phonon object and perform quantum simulation at 300K.
			
	3. Set up Conductivity object and compute thermal conductivity with Quasi Harmonic Green Kubo (QHGK) method.
			
	4. Set up Conductivity object and compute diffusivity with QHGK method.
   
    5. Visualize intermediate quantities from QHGK simulations. 

- To compute 2<sup>nd</sup> and 3<sup>rd</sup> order force constants with LAMMPS PHONON, navigate to this directory and execute:
```console
./mpirun -np 8 /path/to/lammps/src/lmp_mpi < in.aSi512 > aSi512.log 
```
- To comput 2<sup>nd</sup> and 3<sup>rd</sup> order force constants with speed-up LAMMPS PHONON, navigate to this directory and execute:
```console
./mpirun -np 8 /path/to/lammps/src/lmp_mpi < in.aSi512_speed_up > aSi512_speed_up.log 
```
- To perform thermal transport simulation after computing force constants, navigate to this directory and execute:
```python
python thermal_conductivity.py
```
- To access data computed during simulations, navigate to this folder: ***ALD_Si_512***
- Warning: While computing force constants using LAMMPS with a triclinic (non-orthogonal) cell, it follows a strict right-handed cell convention. More information about the cell conventioncan be found [here](https://docs.lammps.org/Howto_triclinic.html). The unit cell of the structure used in this example has been made based on the right-handed cell convention. Please be aware of this rule if lammps inputs were prepared from scratch. Alternatively, it is welcome to refer our [carbon nanotube example](https://github.com/nanotheorygroup/kaldo/tree/main/examples/carbon_nanotube_Tersoff_LAMMPS) where we imposed this convention and prepared lammps input files via a python script.
 
