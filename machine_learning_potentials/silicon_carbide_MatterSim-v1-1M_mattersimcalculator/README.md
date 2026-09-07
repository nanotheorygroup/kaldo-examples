### Computing Thermal Conductivity of Silicon Carbide with MatterSim-v1-1M:

> Input data descriptions for the `MatterSim-v1-1M` potential file can be found [here](https://github.com/microsoft/mattersim).  
> Running `uv run python thermal_conductivity.py` requires [MatterSim](https://github.com/microsoft/mattersim) and [kALDo](https://github.com/nanotheorygroup/kaldo) to be installed.

- Execute `uv run python thermal_conductivity.py` to calculate the thermomechanical properties of Silicon Carbide with MatterSim-v1-1M.

- The calculation proceeds as follows:
  - The SiC structure is created using the Materials Project structure, sourced [here](https://next-gen.materialsproject.org/materials/mp-8062).
  
  - The 2nd and 3rd order force constants are calculated with `MatterSim-v1-1M` and MatterSimCalculator.
  
  - The phonon object is created using a 15x15x15 k-point mesh and quantum simulation is conducted at 300 K.
  
  - The thermal conductivity is then calculated using both direct inversion and with isotopic scattering included.
 
- Navigate to `ALD_SiC_MatterSim/15_15_15/` to view calculated properties during simulations.
- Navigate to `plots/15_15_15/` to view figures generated during simulations.
  - Alternatively, use the jupyter notebook `kALDo_with_MatterSim_gallery.ipynb` to visualize all properties calculated during simulations.
 
 Reference Thermal Conductivity (10x10x10 2nd order supercell, 5x5x5 3rd order supercell, 15x15x15 k-point mesh):
  - ***434.8 W/m-K (Inversion), 373.7 W/m-K (Isotopic)***
