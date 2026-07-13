# Example: bulk silicon, force constants extracted with pheasy
# Computes: phonons and thermal conductivity (BTE, inverse and RTA)
# Uses: 2nd and 3rd order force constants fitted by pheasy from DFT forces

# Import necessary packages

import numpy as np
from kaldo.forceconstants import ForceConstants
from kaldo.phonons import Phonons
from kaldo.conductivity import Conductivity

# Replicate the unit cell 'nrep' times to match the supercell pheasy fit on
nrep = 3
supercell = np.array([nrep, nrep, nrep])

# Load force constants from the pheasy working directory
# 'fc_pheasy' holds POSCAR, FORCE_CONSTANTS (2nd order, phonopy-style text)
# and FORCE_CONSTANTS_3RD (3rd order, ShengBTE-style text)
force_constants = ForceConstants.from_folder(
    folder="fc_pheasy",
    supercell=supercell,
    format="pheasy",
)


# -- Set up the phonon object and the harmonic property calculations -- #

# Configure phonon object
# 'kpts': number of k-points in each direction
# 'is_classic': specify if the system is classic, True for classical and False for quantum
# 'temperature': temperature (Kelvin) at which the simulation is performed
# 'storage': format to store phonon properties ('formatted' for ASCII data, 'numpy'
#            for python numpy arrays and 'memory' for quick calculations, no data stored)
k_points = 7  # 'k_points' = 7 k-points in each direction
phonons_config = {
    "kpts": [k_points, k_points, k_points],
    "is_classic": False,
    "temperature": 300,  # 'temperature' = 300 K
    "storage": "memory",
}

# Set up phonon object by passing in configuration details and the
# forceconstants object loaded above
phonons = Phonons(forceconstants=force_constants, **phonons_config)


# Calculate conductivity with the direct inversion approach (inverse)
print("\n")
inv_cond_matrix = Conductivity(phonons=phonons, method="inverse").conductivity.sum(
    axis=0
)
print(
    "Bulk thermal conductivity, inverse (W/m/K): ",
    np.mean([inv_cond_matrix[0, 0], inv_cond_matrix[1, 1], inv_cond_matrix[2, 2]]),
)
print("\n")
print("Thermal conductivity tensor (inverse): \n")
print(inv_cond_matrix)


# Calculate conductivity with the relaxation time approximation (RTA)
rta_cond_matrix = Conductivity(phonons=phonons, method="rta").conductivity.sum(axis=0)
print("\n")
print(
    "Bulk thermal conductivity, RTA (W/m/K): ",
    np.mean([rta_cond_matrix[0, 0], rta_cond_matrix[1, 1], rta_cond_matrix[2, 2]]),
)
print("\n")
print("Thermal conductivity tensor (RTA): \n")
print(rta_cond_matrix)
print("\n")
