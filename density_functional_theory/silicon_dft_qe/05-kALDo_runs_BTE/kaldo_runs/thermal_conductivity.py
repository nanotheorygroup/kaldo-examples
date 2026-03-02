# Example: bulk siliocn, Si.pz-vbc.UPF persudo potential
# Computes: phonons and density of states from DFPT
# Uses: DFPT from QE

# Import necessary packages

import numpy as np
from kaldo.forceconstants import ForceConstants
from kaldo.phonons import Phonons
from kaldo.conductivity import Conductivity
import kaldo.controllers.plotter as plotter

# Replicate the unit cell 'nrep_2nd'=8 times on 2nd order FCs
nrep_2nd = 8
nrep_3rd = 3
supercell = np.array([nrep_2nd, nrep_2nd, nrep_2nd])
third_supercell = np.array([nrep_3rd, nrep_3rd, nrep_3rd])

# Load in Fcs
force_constants = ForceConstants.from_folder(
    supercell=supercell,
    third_supercell=third_supercell,
    is_acoustic_sum=True,
    folder="fc_DFT",
    format="qe-sheng",
)


# -- Set up the phonon object and the harmonic property calculations -- #

# Configure phonon object
# 'k_points': number of k-points
# 'is_classic': specify if the system is classic, True for classical and False for quantum
# 'temperature: temperature (Kelvin) at which simulation is performed
# 'folder': name of folder containing phonon property and thermal conductivity calculations
# 'storage': Format to storage phonon properties ('formatted' for ASCII format data, 'numpy'
#            for python numpy array and 'memory' for quick calculations, no data stored")


# Define the k-point mesh using 'kpts' parameter
k_points = 14  # 'k_points'= 9 k points in each direction
phonons_config = {
    "kpts": [k_points, k_points, k_points],
    "is_classic": False,
    "temperature": 300,  # 'temperature'=300K
    "folder": "ALD_si_bulk",
    "storage": "numpy",
}

# Set up phonon object by passing in configuration details and the forceconstants object computed above
phonons = Phonons(forceconstants=force_constants, **phonons_config)


# Compute phonons, density of state and other harmonic properties
plotter.plot_dispersion(phonons, n_k_points=300, with_velocity=True, is_showing=False)
plotter.plot_dos(phonons, bandwidth=0.01, filename="dos")


# Calculate conductivity with direct inversion approach (inverse)
print("\n")
inv_cond_matrix = Conductivity(phonons=phonons, method="inverse").conductivity.sum(
    axis=0
)
print(
    "Bulk thermal conductivity (W/m/K): ",
    np.mean([inv_cond_matrix[0, 0], inv_cond_matrix[1, 1], inv_cond_matrix[2, 2]]),
)
print("\n")
print("Thermal condutivity tensor: \n")
print(inv_cond_matrix)


# Trun on include_isotopes in phonon object
phonons.include_isotopes = True

inv_cond_matrix_iso = Conductivity(phonons=phonons, method="inverse").conductivity.sum(
    axis=0
)
print(
    "Bulk thermal conductivity with iso(W/m/K): ",
    np.mean(
        [
            inv_cond_matrix_iso[0, 0],
            inv_cond_matrix_iso[1, 1],
            inv_cond_matrix_iso[2, 2],
        ]
    ),
)
print("\n")
print("Thermal condutivity tensor with iso: \n")
print(inv_cond_matrix_iso)
print("\n")
