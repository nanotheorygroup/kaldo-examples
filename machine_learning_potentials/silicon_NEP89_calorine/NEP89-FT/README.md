## Computing Thermal Conductivity using a Fine-Tuned Neuroevolution Potential (NEP):

> Input data descriptions for the `nep89_finetuned_on_Si.txt` potential file can be found under the `fine_tune/` folder.
> Running `uv run python thermal_conductivity.py` requires [ASE](https://ase-lib.org), [kALDo](https://github.com/nanotheorygroup/kaldo), and [calorine](https://calorine.materialsmodeling.org) to be installed.

- Execute `uv run python thermal_conductivity.py` to calculate the thermomechanical properties of Silicon using the fine-tuned NEP potential.

- The calculation proceeds as follows:
  - The Si structure is created using the Materials Project structure, sourced [here](https://next-gen.materialsproject.org/materials/mp-149).
  
  - The 2nd and 3rd order force constants are calculated with 'nep89_finetuned_on_Si.txt' using calorine.
  
  - The phonon object is created using a 15x15x15 k-point mesh and quantum simulation is conducted at 300 K.
  
  - The thermal conductivity is then calculated using both direct inversion and with isotopic scattering included.
 
- Navigate to `ALD_Si_NEP/15_15_15/` to view calculated properties during simulations.
- Navigate to `plots/15_15_15/` to view figures generated during simulations.
  - Alternatively, use the jupyter notebook `kALDo_with_NEP_FT_gallery.ipynb` to visualize all properties calculated during simulations.
 
Reference Thermal Conductivity (10x10x10 2nd order supercell, 5x5x5 3rd order supercell, 15x15x15 k-point mesh):
  - ***124.7 W/m-K (Inversion), 115.4 W/m-K (Isotopic)***
