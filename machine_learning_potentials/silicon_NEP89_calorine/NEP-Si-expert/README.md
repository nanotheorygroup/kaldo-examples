### Computing Thermal Conductivity of Silicon with an Expert Neuroevolution Potential (NEP):

> Input data descriptions for the `nep.txt` potential file can be found [here](https://gitlab.com/brucefan1983/nep-data/-/tree/main/2024_Dong_Si/NEP-iteration-2/predict-2?ref_type=heads).  
> Running `python thermal_conductivity.py` requires [ASE](https://ase-lib.org), [kALDo](https://github.com/nanotheorygroup/kaldo), and [calorine](https://calorine.materialsmodeling.org) to be installed.

- Execute `python thermal_conductivity.py` to calculate the thermomechanical properties of Silicon using the example expert NEP potential.

- The calculation proceeds as follows:
  - The Si structure is created using the Materials Project structure, sourced [here](https://next-gen.materialsproject.org/materials/mp-149).
  
  - The 2nd and 3rd order force constants are calculated with `nep.txt` using calorine.
  
  - The phonon object is created using a 15x15x15 k-point mesh and quantum simulation is conducted at 300 K.
  
  - The thermal conductivity is then calculated using both direct inversion and with isotopic scattering included.
 
- Navigate to `ALD_Si_NEP/15_15_15/` to view calculated properties during simulations.
- Navigate to `plots/15_15_15/` to view figures generated during simulations.
  - Alternatively, use the jupyter notebook `kALDo_with_NEP_gallery.ipynb` to visualize all properties calculated during simulations.
 
Reference Thermal Conductivity (10x10x10 2nd order supercell, 5x5x5 3rd order supercell, 15x15x15 k-point mesh):
  - ***137.1 W/m-K (Inversion), 124.5 W/m-K (Isotopic)***
