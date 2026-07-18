from ase.build import bulk
from ase.filters import StrainFilter
from ase.constraints import FixSymmetry
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
import torch

# Set up orb calculator and its hardware and precision specification
device = "cuda" if torch.cuda.is_available() else "cpu"
orbff = pretrained.orb_v3_conservative_inf_omat(
  device=device,
  precision="float32-high",   # or "float32-highest" / "float64
)
calc = ORBCalculator(orbff, device=device)

raw_atoms = bulk("GaAs", "zincblende", a=5.75)
raw_atoms.calc = calc

# Acess all symbols
symbols = np.array(raw_atoms.get_chemical_symbols())

# Find indices for Ga and As
Ga_idx = np.where(symbols == 'Ga')[0]
As_idx = np.where(symbols == 'As')[0]

# optimize structures persving symmetries
raw_atoms.set_constraint(FixSymmetry(raw_atoms))
sf = StrainFilter(raw_atoms)
dyn = BFGS(sf, trajectory='GaAs.traj')
dyn.run(fmax=0.0001)

atoms = read('GaAs.traj')

# Lift the constraint so supercell repcliation 
# procceed
atoms.set_constraint([])

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

Cij = forceconstants.elastic_prop()
print('\n')
print("C11: %.1f GPa" %Cij[0, 0, 0, 0])
print("C12: %.1f GPa" %Cij[0, 0, 1, 1])
print("C44: %.1f GPa" %Cij[1, 2, 1, 2])
print("Bulk Modulus:  %.1f GPa" %((Cij[0, 0, 0, 0] + 2 * Cij[0, 0, 1, 1])/3))
np.save("Cij.npy", Cij)

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

# Plot dispersion relation and group velocity in each direction
plotter.plot_dispersion(phonons,n_k_points=300, is_showing=False)

# Plot total and particial dos
plotter.plot_dos(phonons,p_atoms=None, bandwidth=0.01, filename='dos')
plotter.plot_dos(phonons,p_atoms=list(Ga_idx), bandwidth=0.01, filename='pdos_Ga')
plotter.plot_dos(phonons,p_atoms=list(As_idx), bandwidth=0.01, filename='pdos_As')


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
