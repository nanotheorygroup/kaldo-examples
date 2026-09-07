### Computing Thermal Conductivity of Aluminium Nitride with ACE (Atomic Cluster Expansion):

> Input data descriptions for the `ACE` potential file can be found [here](https://pacemaker.readthedocs.io/en/feature-docs/pyace.html).  
> Running `uv run python thermal_conductivity.py` requires [pyace](https://pacemaker.readthedocs.io/en/feature-docs/pyace.html) and [kALDo](https://github.com/nanotheorygroup/kaldo) to be installed:

```console
# 1. Create and activate a virtual environment with Python 3.10
uv venv ace --python 3.10
source ace/bin/activate

# 2. Install cmake 
# and install the specific setuptools version
uv pip install cmake "setuptools<82.0.0"

# 3. Clone and install TensorPotential from source
git clone https://github.com/ICAMS/TensorPotential.git
cd TensorPotentia/
uv pip install .
cd ../

# 4. Clone and install python-ace from source
git clone https://github.com/ICAMS/python-ace.git
cd python-ace/
uv pip install .
cd ../

# 5. Finally install kALDo from GitHub
uv pip install "git+https://github.com/nanotheorygroup/kaldo"
```

- Execute `uv run python phonon.py` to calculate phonon dipersions and elastic properties of Aluminium Nitride with ACE.

- The calculation proceeds as follows:
  
  - The AlN structure is created using the Materials Project structure, sourced [here](https://next-gen.materialsproject.org/materials/mp-661).
  
  - The [equation of states](https://ase-lib.org/ase/eos.html) is carried out with `pycae` and [ASE](https://ase-lib.org/) to obtain optimized lattice.
  
  - The optimized position of Aluminium Nitride is obtained with a [fixed box BFGS](https://ase-lib.org/ase/optimize.html) algorithm on top of the optimized lattice.

  - The 2nd and order force constants are calculated with `pyace` and PyACECalculator.

  - The elastic constants of Aluminium Nitride is computed based on Born-Huang long wavelength method.

  - The phonon dispersions and density of states are computed using kALDo.


- Execute `uv run python thermal_conductivity.py` to calculate the thermal conductivies of Aluminium Nitride with ACE potential.

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
