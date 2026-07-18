### Computing Thermal Conductivity of Silicon with an Universal Neuroevolution Potential (NEP):

> Input data descriptions for the `nep89_20250409.txt` potential file can be found [here](https://github.com/brucefan1983/GPUMD/tree/master/potentials/nep/nep89_20250409).  
> Running `uv run python thermal_conductivity.py` requires [ASE](https://ase-lib.org), [kALDo](https://github.com/nanotheorygroup/kaldo), and [calorine](https://calorine.materialsmodeling.org) to be installed.

- Execute `uv run python thermal_conductivity.py` to calculate the thermomechanical properties of Silicon using the NEP89 potential.

- The calculation proceeds as follows:
  - The Si structure is created using the Materials Project structure, sourced [here](https://next-gen.materialsproject.org/materials/mp-149).
  
  - The 2nd and 3rd order force constants are calculated with `nep89_20250409.txt` using calorine.
  
  - The phonon object is created using a 15x15x15 k-point mesh and quantum simulation is conducted at 300 K.
  
  - The thermal conductivity is then calculated using both direct inversion and with isotopic scattering included.
 
- Navigate to `ALD_Si_NEP/15_15_15/` to view calculated properties during simulations.
- Navigate to `plots/15_15_15/` to view figures generated during simulations.
  - Alternatively, use the jupyter notebook `kALDo_with_NEP_gallery.ipynb` to visualize all properties calculated during simulations.
 
 Reference Thermal Conductivity (10x10x10 2nd order supercell, 5x5x5 3rd order supercell, 15x15x15 k-point mesh):
  - ***41.9 W/m-K (Inversion), 39.8 W/m-K (Isotopic)***
