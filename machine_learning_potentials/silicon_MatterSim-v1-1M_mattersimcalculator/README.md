### Computing Coefficients of Thermal Expansion of Silicon with MatterSim-v1-1M:

> Input data descriptions for the `MatterSim-v1-1M` potential file can be found [here](https://github.com/microsoft/mattersim).  
> Running `python thermal_conductivity.py` requires [MatterSim](https://github.com/microsoft/mattersim) and [kALDo](https://github.com/nanotheorygroup/kaldo) to be installed.

- Execute `python thermal_conductivity.py` to calculate the lattice constants, free energies and thermal expansion coefficients of Siliconwith MatterSim-v1-1M.

- The calculation proceeds as follows:
  - The Si structure is created using the Materials Project structure, sourced [here](https://next-gen.materialsproject.org/materials/mp-149).
  
  - The 2nd order force constants are calculated with `MatterSim-v1-1M` and MatterSimCalculator.
  
  - The quasiharmonic approximations are conducted from 0 to 1800K on 5K increments.
   
- Navigate to `kaldo_runs` to view calculated properties during simulations.
  - Alternatively, use the jupyter notebook `kALDo_with_MatterSim_gallery.ipynb` to visualize all properties calculated during simulations.
 
