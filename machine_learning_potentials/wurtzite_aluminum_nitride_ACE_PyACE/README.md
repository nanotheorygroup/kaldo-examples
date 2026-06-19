### Computing Thermal Conductivity of Aluminium Nitride with ACE (Atomic Cluster Expansion):

> Input data descriptions for the `ACE` potential file can be found [here](https://pacemaker.readthedocs.io/en/feature-docs/pyace.html).  
> Running `python thermal_conductivity.py` requires [pyace](https://pacemaker.readthedocs.io/en/feature-docs/pyace.html) and [kALDo](https://github.com/nanotheorygroup/kaldo) to be installed:

```console
# Create conda enviornment
conda create --name ace python==3.10

# Activate the enviornment and roll back
# set up tools that contained pkg_resources
conda activate ace
conda install cmake
pip install --force-reinstall "setuptools<82.0.0"

# Install TensorPotential from source
git clone https://github.com/ICAMS/TensorPotential.git
cd TensorPotential/
cd ../

# Install python-ace form source
git clone https://github.com/ICAMS/python-ace.git
cd python-ace/
pip install .
cd ../
 
# Finally install kALDo
pip install git+https://github.com/nanotheorygroup/kaldo
```

- Execute `python phonon.py` to calculate phonon dipersions and elastic properties of Aluminium Nitride with ACE.

- The calculation proceeds as follows:
  
  - The AlN structure is created using the Materials Project structure, sourced [here](https://next-gen.materialsproject.org/materials/mp-661).
  
  - The [equation of states](https://ase-lib.org/ase/eos.html) is carried out with `pycae` and [ASE](https://ase-lib.org/) to obtain optimized lattice.
  
  - The optimized position of Aluminium Nitride is obtained with a [fixed box BFGS](https://ase-lib.org/ase/optimize.html) algorithm on top of the optimized lattice.

  - The 2nd and order force constants are calculated with `pyace` and PyACECalculator.

  - The elastic constants of Aluminium Nitride is computed based on Born-Huang long wavelength method.

  - The phonon dispersions and density of states are computed using kALDo.


- Execute `python thermal_conductivity.py` to calculate the thermal conductivies of Aluminium Nitride with ACE potential.

- The calculation proceeds as follows:
  - The AlN structure is created using the Materials Project structure, sourced [here](https://next-gen.materialsproject.org/materials/mp-661).
  
  - The 2nd and 3rd order force constants are calculated with `pyace` and PyACECalculator.
  
  - The phonon object is created using a 15x15x9 k-point mesh and quantum simulation is conducted at 300 K.
  
  - The thermal conductivity is then calculated using both direct inversion and with isotopic scattering included.
 
- Navigate to `ALD_AlN_ACE/15_15_9/` to view calculated properties during simulations.
- Navigate to `plots/15_15_9/` to view figures generated during simulations.
  - Alternatively, use the jupyter notebook `kALDo_with_ace_gallery.ipynb` to visualize all properties calculated during simulations.
 
 Reference Thermal Conductivity (15x15x9 2nd order supercell, 4x4x3 3rd order supercell, 15x15x9 k-point mesh):
  - ***260.3 W/m-K (Inversion), 259.9 W/m-K (Isotopic)***
