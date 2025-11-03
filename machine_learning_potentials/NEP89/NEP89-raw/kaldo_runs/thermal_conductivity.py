from ase.build import bulk
from ase.constraints import StrainFilter
from ase.io import read
from ase.optimize import BFGS
from calorine.calculators import CPUNEP
from kaldo.conductivity import Conductivity
from kaldo.forceconstants import ForceConstants
from kaldo.phonons import Phonons
import kaldo.controllers.plotter as plotter
import matplotlib.pyplot as plt
import numpy as np

# We start from the atoms object
# the Si structure is taken from
# material project: 
# https://next-gen.materialsproject.org/materials/mp-149
raw_atoms = bulk('Si', 'diamond', a=5.44)
nep_calculator = CPUNEP('nep89_20250409.txt')
raw_atoms.calc = nep_calculator
sf = StrainFilter(raw_atoms)
dyn = BFGS(sf, trajectory='Si.traj')
dyn.run(fmax=0.0001)
atoms = read('Si.traj')

# Config super cell and calculator input
second_supercell = np.array([10, 10, 10])
third_supercell = np.array([5, 5, 5])

# Create a finite difference object
forceconstants_config  = {'atoms':atoms,'supercell': second_supercell, 
                          'third_supercell':third_supercell, 'folder':'fd_NEP/'}
forceconstants = ForceConstants(**forceconstants_config)

# Compute 2nd and 3rd IFCs with the defined calculators
forceconstants.second.calculate(nep_calculator, delta_shift=3e-2)
forceconstants.third.calculate(nep_calculator, delta_shift=3e-2)

Cij = forceconstants.elastic_prop()
print("C11: %.1f GPa" %Cij[0, 0, 0, 0])
print("C12: %.1f GPa" %Cij[0, 0, 1, 1])
print("C44: %.1f GPa" %Cij[1, 2, 1, 2])
print("Bulk Modulus:  %.1f GPa" %((Cij[0, 0, 0, 0] + 2 * Cij[0, 0, 1, 1])/3))
np.save("Cij.npy", Cij)


# Define k-point grids, temperature
# and the assumption for the
# phonon poluation (i.e classical vs. quantum)
k = 15
kpts = [k, k, k]
temperature = 300
is_classic = False
k_label = str(k) + '_' + str(k) + '_' + str(k)

# Create a phonon object
phonons = Phonons(forceconstants=forceconstants,
                kpts=kpts,
                is_classic=is_classic,
                temperature=temperature,
                folder='ALD_Si_NEP',
                storage='numpy')


# Plot dispersion relation and group velocity in each direction
plotter.plot_dispersion(phonons,n_k_points=300, is_showing=False)
plotter.plot_dos(phonons,p_atoms=None, bandwidth=0.05, filename='dos')

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
