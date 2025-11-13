from ase.build import bulk
from ase.io import read
from kaldo import quasiharmonic as qha
from loguru import logger
from mattersim.forcefield import MatterSimCalculator
import numpy as np
import os
import torch

# Denote device used for potential
device = "cuda" if torch.cuda.is_available() else "cpu"
logger.info(f"Running MatterSim on {device}")

# Set up mattersim calculator
calc =  MatterSimCalculator(device=device)


# Set up cubic system for silicon
atoms = bulk('Si', a=5.432, cubic=True)
atoms.calc = calc

#   Run quasi-harmonic approximation (QHA) simulations:
#   - Computes temperature-dependent lattice constants, Helmholtz free energies
#     and linear thermal expansion coefficients for bulk silicon.
#   - Temperatures are sampled from 0 K to 1800 K every 5 K
#     (np.linspace(0, 1800, 361)).
#   - supercell controls the size of the supercell used for force-constant
#     calculations (here 6×6×6); larger values improve accuracy but are slower.
#   - kpts sets the Brillouin-zone sampling for phonon calculations.
#   - lattice_range and n_lattice_points control how densely the code samples
#     the lattice parameter grid around the initial structure.
#   - n_fine_points defines how fine the grid is when minimizing the fitted
#     free-energy surface; increasing it gives smoother curves at higher cost.
results = qha.calculate_qha(atoms=atoms, 
        calculator=calc, temperatures=np.linspace(0, 1800, 361), 
        supercell=(6, 6, 6), kpts=(12, 12, 12), symmetry=None, 
        lattice_range=0.01, n_lattice_points=11, 
        n_fine_points=10**(5))

# Save key results
np.save('L_T.npy', results['lattice_constants'])
np.save('F_T.npy', results['free_energies'])
np.save('alpha_T.npy', results['thermal_expansion'])
