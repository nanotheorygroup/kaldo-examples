# Example: bulk germanium, Ge.pz-bhs.UPF persudo potential
# Computes: phonons and density of states from DFPT
# Uses: DFPT from QE

# Import necessary packages

import numpy as np
from kaldo.forceconstants import ForceConstants
from kaldo.phonons import Phonons
from kaldo.conductivity import Conductivity
import kaldo.controllers.plotter as plotter
import tarfile

# Etract tar ball
tar = tarfile.open("fc_DFT_with_NAC.tar.gz")
tar.extractall(filter='data')
tar.close()


# Replicate the unit cell 'nrep'=10 times
nrep = 9
supercell = np.array([nrep, nrep, nrep])

# Define loading instructions
# only loading second order force constants
# apply acoustic sum rule when loading 2nd order fc to kALDo
force_constants = ForceConstants.from_folder(
                           supercell=supercell,
                           only_second=True,
                           is_acoustic_sum=True,
                           folder='fc_DFT_with_NAC',
                           format='shengbte-d3q')


# -- Set up the phonon object and the harmonic property calculations -- #

# Configure phonon object
# 'k_points': number of k-points
# 'is_classic': specify if the system is classic, True for classical and False for quantum
# 'temperature: temperature (Kelvin) at which simulation is performed
# 'folder': name of folder containing phonon property and thermal conductivity calculations
# 'storage': Format to storage phonon properties ('formatted' for ASCII format data, 'numpy'
#            for python numpy array and 'memory' for quick calculations, no data stored")


# Define the k-point mesh using 'kpts' parameter
k_points = 18  # 'k_points'= 24 k points in each direction
phonons_config = {'kpts': [k_points, k_points, k_points],
                  'is_classic': False,
                  'is_unfolding':True,
                  'temperature': 300,  # 'temperature'=300K
                  'folder': 'ALD_MgO_phonons_with_NAC',
                  'storage': 'formatted'}

# Set up phonon object by passing in configuration details and the forceconstants object computed above
phonons = Phonons(forceconstants=force_constants, **phonons_config)


# Compute phonons, density of state and other harmonic properties
plotter.plot_dispersion(phonons, n_k_points=300, with_velocity=True, is_showing=False)
plotter.plot_dos(phonons,bandwidth=0.01, filename='dos')
print("Phonons from DFPT done!")
