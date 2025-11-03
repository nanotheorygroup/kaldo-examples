from ase.build import bulk
from ase.constraints import StrainFilter
from ase.io import read
from ase.optimize import BFGS
from kaldo.conductivity import Conductivity
from kaldo.forceconstants import ForceConstants
from kaldo.phonons import Phonons
import kaldo.controllers.plotter as plotter
import matplotlib.pyplot as plt
import numpy as np
from pyace import PyACECalculator

# Set up ace calculator 
ace_calculator = PyACECalculator('w-AlN_ace_2023-06-20.yaml')

# We start from optimized structure
atoms = read('AlN.traj')

# Config super cell and calculator input
second_supercell = np.array([15, 15, 9])
third_supercell = np.array([4, 4, 3])

# Create a finite difference object
forceconstants_config  = {'atoms':atoms,'supercell': second_supercell, 
                          'third_supercell':third_supercell,
                          'folder':'fd_ACE/'}
forceconstants = ForceConstants(**forceconstants_config)

# Compute 2nd and 3rd IFCs with the defined calculators
forceconstants.second.calculate(ace_calculator, delta_shift=1e-4)
forceconstants.third.calculate(ace_calculator, delta_shift=1e-4)

# Define k-point grids, temperature
# and the assumption for the
# phonon poluation (i.e classical vs. quantum)

kpts = [15, 15, 9]
temperature = 300
is_classic = False
k_label = str(kpts[0]) + '_' + str(kpts[1]) + str(kpts[2])

# Create a phonon object
phonons = Phonons(forceconstants=forceconstants,
                kpts=kpts,
                is_classic=is_classic,
                temperature=temperature,
                folder='ALD_AlN_ACE',
                storage='numpy')

# Calculate conductivity with direct inversion approach (inverse)
print('\n')
inv_cond_matrix = (Conductivity(phonons=phonons, method='inverse').conductivity.sum(axis=0))
print('Bulk thermal conductivity (W/m/K): ', np.mean([inv_cond_matrix[0,0], inv_cond_matrix[1,1], inv_cond_matrix[2,2]]))
print('\n')
print('Thermal condutivity tensor: \n')
print(inv_cond_matrix)


# Trun on include_isotopes in phonon object
phonons.include_isotopes = True

inv_cond_matrix_iso = (Conductivity(phonons=phonons, method='inverse').conductivity.sum(axis=0))
print('Bulk thermal conductivity with iso(W/m/K): ', np.mean([inv_cond_matrix_iso[0,0], inv_cond_matrix_iso[1,1], inv_cond_matrix_iso[2,2]]))
print('\n')
print('Thermal condutivity tensor with iso: \n')
print(inv_cond_matrix_iso)
print('\n')
