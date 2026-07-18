### Computing Thermal Conductivity of Gallium Arsenide with orb-v3:

> Input data descriptions for the `orb-v3` potential file can be found [here](https://github.com/orbital-materials/orb-models).  
> Running `uv run python thermal_conductivity.py` requires [orb-models](https://github.com/orbital-materials/orb-models) and [kALDo](https://github.com/nanotheorygroup/kaldo) to be installed.

- Execute `uv run python thermal_conductivity.py` to calculate the thermal conductivies of Gallium Arsenide with orb-v3.

- The calculation proceeds as follows:
  - The GaAs structure is created using the Materials Project structure, sourced [here](https://next-gen.materialsproject.org/materials/mp-2534).
  
  - The 2nd and 3rd order force constants are calculated with `orb-v3` and ORBCalculator.
  
  - The phonon object is created using a 12x12x12 k-point mesh and quantum simulation is conducted at 300 K.
  
  - The thermal conductivity is then calculated using both direct inversion and with isotopic scattering included.
 
- Navigate to `ALD_GaAs_orb_v3_conservative_inf_omat/12_12_12/` to view calculated properties during simulations.
- Navigate to `plots/12_12_12/` to view figures generated during simulations.
  - Alternatively, use the jupyter notebook `kALDo_with_orb_gallery.ipynb` to visualize all properties calculated during simulations.
 
 Reference Thermal Conductivity (12x12x12 2nd order supercell, 6x6x6 3rd order supercell, 12x12x12 k-point mesh):
  - ***32.8 W/m-K (Inversion), 31.7 W/m-K (Isotopic)***
