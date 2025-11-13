### Computing Coefficients of Thermal Expansion of Silicon with MatterSim-v1-1M:

> Input data descriptions for the `MatterSim-v1-1M` potential file can be found [here](https://github.com/microsoft/mattersim).  
> Running `quasi_harmonic_approximations.py` requires [MatterSim](https://github.com/microsoft/mattersim) and [kALDo](https://github.com/nanotheorygroup/kaldo) to be installed.

- Execute `python quasi_harmonic_approximations.py` to calculate the lattice constants, free energies and thermal expansion coefficients of Silicon with MatterSim-v1-1M.

- The calculation proceeds as follows:
  - The Si structure is created using the Materials Project structure, sourced [here](https://next-gen.materialsproject.org/materials/mp-149).
  
  - The 2nd order force constants are calculated with `MatterSim-v1-1M` and MatterSimCalculator.
  
  - The quasiharmonic approximations are conducted from 0 to 1800K, with a 6x6x6 supercell and 1 percent purtbued volumes.
   
- Navigate to `kaldo_runs` to view calculated properties during simulations.
  - Alternatively, use the jupyter notebook `kALDo_with_MatterSim_gallery.ipynb` to visualize all properties calculated during simulations.
 
