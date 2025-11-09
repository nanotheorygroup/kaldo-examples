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

# We start from the atoms object for w-AlN
raw_atoms = bulk('AlN','wurtzite', a=3.13, c=5.02)
ace_calculator = PyACECalculator('w-AlN_ace_2023-06-20.yaml')
raw_atoms.calc = ace_calculator
sf = StrainFilter(raw_atoms)
dyn = BFGS(sf, trajectory='AlN.traj')
dyn.run(fmax=0.0001)
atoms = read('AlN.traj')
path = atoms.cell.bandpath('GKMGA', npoints=300)

# Config super cell and calculator input
second_supercell = np.array([15, 15, 9])

# Create a finite difference object
forceconstants_config  = {'atoms':atoms,'supercell': second_supercell, 'folder':'fd_ACE/'}
forceconstants = ForceConstants(**forceconstants_config)

# Compute 2nd IFCs with ace alculators
forceconstants.second.calculate(ace_calculator, delta_shift=1e-4)
Cij = forceconstants.elastic_prop()
print('\n')
print("C11: %.1f GPa" %Cij[0, 0, 0, 0])
print("C12: %.1f GPa" %Cij[0, 0, 1, 1])
print("C44: %.1f GPa" %Cij[1, 2, 1, 2])
np.save("Cij.npy", Cij)

# Define k-point grids, temperature
# and the assumption for the
# phonon poluation (i.e classical vs. quantum)
kpts = [15, 15 , 9]
temperature = 300
is_classic = False
k_label = str(kpts[0]) + '_' + str(kpts[1]) + '_' + str(kpts[2])

# Create a phonon object
phonons = Phonons(forceconstants=forceconstants,
                kpts=kpts,
                is_classic=is_classic,
                temperature=temperature,
                folder='ALD_AlN_ACE',
                storage='numpy')


# Plot dispersion relation and group velocity in each direction
plotter.plot_dispersion(phonons,n_k_points=300, is_showing=False, manually_defined_path=path)
plotter.plot_dos(phonons,p_atoms=None, bandwidth=0.01, filename='dos')
plotter.plot_dos(phonons,p_atoms=[0], bandwidth=0.01, filename='pdos_Al')
plotter.plot_dos(phonons,p_atoms=[1], bandwidth=0.01, filename='pdos_N')
