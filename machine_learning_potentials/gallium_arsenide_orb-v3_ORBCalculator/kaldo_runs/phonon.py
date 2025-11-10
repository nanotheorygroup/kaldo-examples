from ase.build import bulk
from ase.eos import EquationOfState
from ase.io import read
from ase.io.trajectory import Trajectory
from ase.optimize import BFGS
from ase.units import kJ
from kaldo.forceconstants import ForceConstants
from kaldo.phonons import Phonons
import kaldo.controllers.plotter as plotter
import numpy as np
import os
from orb_models.forcefield import pretrained
from orb_models.forcefield.calculator import ORBCalculator
import glob
import shutil
import warnings
warnings.filterwarnings("ignore")


# Create atoms with rough guess of lattice constant
raw_atoms = bulk("GaAs", "zincblende", a=5.75)

# Acess all symbols
symbols = np.array(raw_atoms.get_chemical_symbols())

# Find indices for Ga and As
Ga_idx = np.where(symbols == 'Ga')[0]
As_idx = np.where(symbols == 'As')[0]


# Set up orb calculator and its hardware and precision specification
device="cuda"
orbff = pretrained.orb_v3_conservative_inf_omat(
  device=device,
  precision="float32-highest",   # or "float32-highest" / "float64
)
calc = ORBCalculator(orbff, device=device)

# Allocate calculator to atom object
raw_atoms.calc = calc

# Get cell for raw atoms
cell = raw_atoms.get_cell()

# Set up trajectory object
traj = Trajectory('GaAs_eos.traj', 'w')

# Change the cell by ± 5 %
for x in np.linspace(0.95, 1.05, 100):
    raw_atoms.set_cell(cell * x, scale_atoms=True)
    raw_atoms.get_potential_energy()
    traj.write(raw_atoms)

configs = read('GaAs_eos.traj', index=":")

# Extract volumes and energies:
volumes = [ag.get_volume() for ag in configs]
energies = [ag.get_potential_energy() for ag in configs]
eos = EquationOfState(volumes, energies)

# Perform fitting
v0, e0, B = eos.fit()

# Derive optimal lattice constans
a = (4 * v0)**(1 / 3.0)
print('Optimized lattice constants: ' + '{0:.5f} angstrom'.format(a))


# Targets: directory "plots", file "GaAs.traj", and any "fd_*" files
paths = ['plots', 'GaAs_opt.traj', 'GaAs_eos.traj'] + glob.glob('fd_*')
for p in paths:
    if os.path.isdir(p):
        shutil.rmtree(p)
    elif os.path.isfile(p):
        os.remove(p)

# We start from the atoms object
atoms_with_optimal_cell = bulk("GaAs", "zincblende", a=a)
atoms_with_optimal_cell.calc = calc

# Perform geometry optimization varying both the cell and positions
dyn = BFGS(atoms_with_optimal_cell, trajectory='GaAs_opt.traj')
dyn.run(fmax=0.0001)
atoms = read('GaAs_opt.traj')

# Config super cell and calculator input
second_supercell = np.array([12, 12, 12])

# Create a finite difference object
forceconstants_config  = {'atoms':atoms,'supercell': second_supercell
                          , 'folder':'fd_orb_v3_conservative_inf_omat/'}
forceconstants = ForceConstants(**forceconstants_config)

# Compute 2nd and 3rd IFCs with the defined calculators
forceconstants.second.calculate(calc , delta_shift=5e-2)

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
                folder='ALD_GaAs_orb_v3_conservative_inf_omat/',
                storage='numpy')


# Plot dispersion relation and group velocity in each direction
plotter.plot_dispersion(phonons,n_k_points=300, is_showing=False)

# Plot total and particial dos
plotter.plot_dos(phonons,p_atoms=None, bandwidth=0.01, filename='dos')
plotter.plot_dos(phonons,p_atoms=list(Ga_idx), bandwidth=0.01, filename='pdos_Ga')
plotter.plot_dos(phonons,p_atoms=list(As_idx), bandwidth=0.01, filename='pdos_As')
