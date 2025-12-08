### Compute Gibbs Free Energy of MgO Using Quasi-Harmonic Approximation with MatterSim

> More details on MatterSim potential file can be found [here](https://github.com/microsoft/mattersim).  
> Running `python quasi_harmonic_approximations.py` requires [MatterSim](https://github.com/microsoft/mattersim) and [kALDo](https://github.com/nanotheorygroup/kaldo) to be installed with Python 3.10+.

Execute `python quasi_harmonic_approximations.py` to calculate Gibbs free energy and lattice constant of MgO under a range of temperatures with MatterSim. 

This calculation proceeds as follows:

- The structure of MgO is constructured by [ASE](https://ase-lib.org)
- MatterSim potential is imported and attached to the system. 
- Quasi-harmonic approximation simulation is run by `kaldo.quasiharmonic.calculate_qha`. At each temperature, it will run through a series of calculation on free energy using quasi-harmonic approximation with a range of lattice parameters, and then the min free energy and its corresponding lattice parameter is obtained by curve-fitting. 

This gives Gibbs free energy, lattice constant and thermal expansion coefficient from 0K to 1000K. 

Finally, all the results can be visualized in the Jupyter notebook `kALDo_with_mattersim_gallery.ipynb`. 

