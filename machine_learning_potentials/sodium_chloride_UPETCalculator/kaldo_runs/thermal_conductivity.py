from ase.build import bulk
from ase.constraints import StrainFilter
from ase.constraints import FixSymmetry
from ase.io import read
from ase.optimize import BFGS
from kaldo.forceconstants import ForceConstants
from kaldo.phonons import Phonons
import kaldo.controllers.plotter as plotter
from kaldo.conductivity import Conductivity
import matplotlib.pyplot as plt
import numpy as np
import os
from upet.calculator import UPETCalculator

# Set up calculator
calc = UPETCalculator(model="pet-mad-s", device="cuda")

# Create NaCl cubic structure
raw_atoms = bulk("NaCl", "rocksalt", a=5.59)
raw_atoms.calc = calc

# optimize structures persving symmetries
raw_atoms.set_constraint(FixSymmetry(raw_atoms))
sf = StrainFilter(raw_atoms)
dyn = BFGS(sf, trajectory='NaCl.traj')
dyn.run(fmax=0.0001)

# Read in optimized structure but lift the constraint for supercell
atoms = read('NaCl.traj')
atoms.set_constraint()
print('\n')
print('Optimized Lattices: %.2f Å' % (
    atoms.cell.cellpar()[0] * np.sqrt(2)))

# Config super cell and calculator input
second_supercell = np.array([12, 12, 12])
third_supercell = np.array([4, 4, 4])

# Create a finite difference object
forceconstants_config  = {'atoms':atoms,
                          'supercell': second_supercell,
                          'third_supercell': third_supercell,  
                          'folder':'fd_upet/'}
forceconstants = ForceConstants(**forceconstants_config)

# Compute 2nd aIFCs with the defined calculators
forceconstants.second.calculate(calc , delta_shift=3e-2)
forceconstants.third.calculate(calc , delta_shift=3e-2)

Cij = forceconstants.elastic_prop()
print('\n')
print("C11: %.1f GPa" %Cij[0, 0, 0, 0])
print("C12: %.1f GPa" %Cij[0, 0, 1, 1])
print("C44: %.1f GPa" %Cij[1, 2, 1, 2])
print("Bulk Modulus:  %.1f GPa" %((Cij[0, 0, 0, 0] + 2 * Cij[0, 0, 1, 1])/3))
print('\n')

np.save("Cij.npy", Cij)
# Define k-point grids, temperature
# and the assumption for the
# phonon poluation (i.e classical vs. quantum)
kpts = np.array([12, 12, 12])
temperature = 300
is_classic = False

# Create a phonon object
phonons = Phonons(forceconstants=forceconstants,
                kpts=kpts,
                is_classic=is_classic,
                temperature=temperature,
                folder='ALD_NaCl_upet/',
                storage='numpy')

# Plot dispersion relation and group velocity in each direction
plotter.plot_dispersion(phonons,n_k_points=300, is_showing=False)
plotter.plot_dos(phonons,p_atoms=None, bandwidth=0.01, filename='dos')
plotter.plot_dos(phonons,p_atoms=[0], bandwidth=0.01, filename='pdos_Na')
plotter.plot_dos(phonons,p_atoms=[1], bandwidth=0.01, filename='pdos_Cl')

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
