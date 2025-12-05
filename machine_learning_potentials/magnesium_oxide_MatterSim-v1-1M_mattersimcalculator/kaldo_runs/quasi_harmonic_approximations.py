from ase.build import bulk
from ase.io import read
from kaldo import quasiharmonic as qha
from loguru import logger
import mattertune.configs as MC
from mattertune.backbones import (
    MatterSimM3GNetBackboneModule,
)

import numpy as np
import os
import torch

# Denote device used for potential
device = "cuda" if torch.cuda.is_available() else "cpu"
logger.info(f"Running MatterSim on {device}")

# Set up mattersim calculator
model = MC.MatterSimBackboneConfig.draft()
model.pretrained_model = "MatterSim-v1.0.0-1M"
model.graph_convertor = MC.MatterSimGraphConvertorConfig.draft()
model.optimizer = MC.AdamWConfig(lr=1.0e-4)
energy = MC.EnergyPropertyConfig(loss=MC.MSELossConfig(), loss_coefficient=1.0)
forces = MC.ForcesPropertyConfig(loss=MC.MSELossConfig(), loss_coefficient=1.0, conservative=True)
stresses = MC.StressesPropertyConfig(loss=MC.MSELossConfig(), loss_coefficient=1.0, conservative=True)
model.properties = [energy, forces, stresses]
model = MatterSimM3GNetBackboneModule(model)
model.create_model()

calc = model.ase_calculator(device=device if torch.cuda.is_available() else 'cpu')
calc.set_use_double_precision()


# Set up cubic system for silicon
atoms = bulk("MgO", "rocksalt", a=4.273, cubic=True)
atoms.calc = calc

# Run quasi harmonic approximation simulations
results = qha.calculate_qha(atoms=atoms, 
        calculator=calc, temperatures=np.linspace(0, 900, 361), 
        supercell=(3, 3, 3), kpts=(12, 12, 12), symmetry=None, 
        lattice_range=0.01, n_lattice_points=11, 
        n_fine_points=10**(5))

# Save key results
np.save('L_T.npy', results['lattice_constants'])
np.save('F_T.npy', results['free_energies'])
np.save('alpha_T.npy', results['thermal_expansion'])
