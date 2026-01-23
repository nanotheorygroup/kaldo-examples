### Computing Thermal Conductivity of Sodium Chloride with UPET:

> Input data descriptions for the `PET-MAD` potential file can be found [here](https://github.com/lab-cosmo/upet).  
> Running `python thermal_conductivity.py` requires [UPET](https://github.com/lab-cosmo/upet) and [kALDo](https://github.com/nanotheorygroup/kaldo) to be installed.

- Execute `python thermal_conductivity.py` to calculate the thermomechanical properties of Sodium Chloride with UPET.

- The calculation proceeds as follows:
  - The NaCl structure is created using the Materials Project structure, sourced [here](https://next-gen.materialsproject.org/materials/mp-22862).
  
  - The 2nd and 3rd order force constants are calculated with `UPET` and UPETCalculator.
  
  - The phonon object is created using a 12x12x12 k-point mesh and quantum simulation is conducted at 300 K.
  
  - The thermal conductivity is then calculated using both direct inversion and with isotopic scattering included.
 
- Navigate to `ALD_NaCl_pet_mad/12_12_12/` to view calculated properties during simulations.
- Navigate to `plots/12_12_12/` to view figures generated during simulations.
  - Alternatively, use the jupyter notebook `kALDo_with_upet_gallery.ipynb` to visualize all properties calculated during simulations.
 
 Reference Thermal Conductivity (12x12x12 2nd order supercell, 4x4x4 3rd order supercell, 12x12x12 k-point mesh):
  - ***8.0 W/m-K (Inversion), 7.5 W/m-K (Isotopic)***
