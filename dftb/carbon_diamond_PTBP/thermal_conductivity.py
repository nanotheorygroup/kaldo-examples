# Example: carbon diamond, DFTB+ with PTBP parametrization
# Computes: 2nd, 3rd order force constants and thermal conductivity for carbon diamond (2 atoms per cell)
# Uses: ASE, DFTB+
# External files: PTBP Slater-Koster files from https://zenodo.org/records/14289468

# Import necessary packages

from ase.build import bulk
from ase.calculators.dftb import Dftb
from kaldo.conductivity import Conductivity
from kaldo.forceconstants import ForceConstants
from kaldo.phonons import Phonons
import numpy as np
import os

import kaldo.controllers.plotter as plotter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -- Configuration -- #

# Set DFTB_PREFIX to the directory containing the PTBP .skf files.
# Download from: https://zenodo.org/records/14289468
# Reference: Cui, Reuter, Margraf, J. Chem. Theory Comput. (2024)
#            DOI: 10.1021/acs.jctc.4c00228
DFTB_PREFIX = os.environ.get("DFTB_PREFIX", os.path.expanduser("~/dftb/ptbp_skf/"))

# -- Set up the coordinates of the system and the force constant calculations -- #

# Define the system according to ASE style. 'a': lattice parameter (Angstrom)
atoms = bulk('C', 'diamond', a=3.567)

# Replicate the unit cell 'nrep'=3 times
nrep = 3
supercell = np.array([nrep, nrep, nrep])


# Define the DFTB+ calculator with PTBP parametrization.
# MaxAngularMomentum_C='p' matches the carbon valence shell in PTBP (2s2 2p2).
# PolynomialRepulsive uses the repulsive potentials encoded in the PTBP .skf files.
def make_calc():
    return Dftb(
        label='dftb_tmp',
        kpts=(1, 1, 1),
        Hamiltonian_SCC='Yes',
        Hamiltonian_SCCTolerance=1e-5,
        Hamiltonian_MaxSCCIterations=1000,
        Hamiltonian_MaxAngularMomentum_='',
        Hamiltonian_MaxAngularMomentum_C='p',
        Hamiltonian_Filling='Fermi {Temperature [K] = 300}',
        Hamiltonian_SlaterKosterFiles_='Type2FileNames',
        Hamiltonian_SlaterKosterFiles_Prefix=DFTB_PREFIX,
        Hamiltonian_SlaterKosterFiles_Separator='"-"',
        Hamiltonian_SlaterKosterFiles_Suffix='".skf"',
        Hamiltonian_PolynomialRepulsive='SetForAll {Yes}',
        Hamiltonian_ForceEvaluation='dynamics',
    )


# Configure force constant calculator
forceconstants_config = {'atoms': atoms, 'supercell': supercell, 'folder': 'fc_c_diamond'}
forceconstants = ForceConstants(**forceconstants_config)

# Compute 2nd and 3rd IFCs with the defined calculator
# delta_shift: finite difference displacement, in angstrom
forceconstants.second.calculate(make_calc(), delta_shift=1e-4)
forceconstants.third.calculate(make_calc(), delta_shift=1e-4)

# -- Set up the phonon object and the anharmonic properties calculations -- #

# Configure phonon object
# 'kpts': number of k-points in each direction
# 'is_classic': specify if the system is classic, True for classical and False for quantum
# 'temperature': temperature (Kelvin) at which simulation is performed
# 'folder': name of folder containing phonon property and thermal conductivity calculations
# 'storage': Format to store phonon properties ('formatted' for ASCII format data, 'numpy'
#            for python numpy array and 'memory' for quick calculations, no data stored)

# Define the k-point mesh using 'kpts' parameter
k_points = 11
phonons_config = {'kpts': [k_points, k_points, k_points],
                  'is_classic': False,
                  'temperature': 300,
                  'folder': 'ALD_c_diamond',
                  'storage': 'numpy'}

# Set up phonon object by passing in configuration details and the forceconstants object computed above
phonons = Phonons(forceconstants=forceconstants, **phonons_config)

# -- Set up the Conductivity object and thermal conductivity calculations -- #

# Compute thermal conductivity (t.c.) by solving Boltzmann Transport
# Equation (BTE) with the Relaxation Time Approximation (RTA)

# 'phonons': phonon object obtained from the above calculations
# 'method': specify methods to solve for BTE
# ('rta' for RTA, 'sc' for self-consistent and 'inverse' for direct inversion of the scattering matrix)

print('\n')
rta_cond_matrix = Conductivity(phonons=phonons, method='rta').conductivity.sum(axis=0)
print('Conductivity from RTA (W/m-K): %.3f' % (np.mean(np.diag(rta_cond_matrix))))
print(rta_cond_matrix)

# Make plots for quick data visualization
plotter.plot_dispersion(phonons, with_velocity=True, is_showing=False)
plotter.plot_dos(phonons, is_showing=False)
