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
from orb_models.forcefield import pretrained
from orb_models.forcefield.calculator import ORBCalculator

# Set up orb calculator and its hardware and precision specification
device="cuda"
orbff = pretrained.orb_v3_conservative_inf_omat(
  device=device,
  precision="float32-high",   # or "float32-highest" / "float64
)
calc = ORBCalculator(orbff, device=device)

# We start from optimized structure
atoms = read('GaAs_opt.traj')

# Config super cell and calculator input
second_supercell = np.array([12, 12, 12])
third_supercell = np.array([6, 6, 6])

# Create a finite difference object
forceconstants_config  = {'atoms':atoms,'supercell': second_supercell, 
                          'third_supercell':third_supercell,
                          'folder':'fd_orb_v3_conservative_inf_omat/'}
forceconstants = ForceConstants(**forceconstants_config)

# Compute 2nd and 3rd IFCs with the defined calculators
forceconstants.second.calculate(calc, delta_shift=5e-2)
forceconstants.third.calculate(calc, delta_shift=5e-2)

# Define k-point grids, temperature
# and the assumption for the
# phonon poluation (i.e classical vs. quantum)
k = 12
kpts = [k, k, k]
temperature = 300
is_classic = False
k_label = str(k) + '_' + str(k) + '_' + str(k)

# Create a phonon object
phonons = Phonons(forceconstants=forceconstants,
                kpts=kpts,
                is_classic=is_classic,
                temperature=temperature,
                folder='ALD_GaAs_orb_v3_conservative_inf_omat',
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
