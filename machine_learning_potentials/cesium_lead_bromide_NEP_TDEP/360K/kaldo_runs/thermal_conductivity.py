from kaldo.conductivity import Conductivity
from kaldo.forceconstants import ForceConstants
from kaldo.phonons import Phonons
import kaldo.controllers.plotter as plotter
import numpy as np

# Load in force constants from TDEP
tdep_fcs = ForceConstants.from_folder(folder='tdep_fcs_cubic_CsPbBr3', 
                                      supercell=(6, 6, 6),
                                      format='tdep')
 
# Define k-point grids, temperature
# and the assumption for the
# phonon poluation (i.e classical vs. quantum)
kpts = [12, 12, 12]
temperature = 360
is_classic = False
    
# Denote if is computing full QHGK
is_compute_full_QHGK = True

# Create a phonon object
phonons = Phonons(forceconstants=tdep_fcs,
                kpts=kpts,
                is_classic=is_classic,
                temperature=temperature,
                folder='ALD_CsPbBr3_NEP',
                storage='numpy')

# Plot dispersion relation and group velocity in each direction
plotter.plot_dispersion(phonons,n_k_points=300, is_showing=False)
plotter.plot_dos(phonons, bandwidth=0.001)

# Calculate conductivity  with direct inversion approach (inverse)
print('\n')
qhgk_cond = Conductivity(phonons=phonons, method='qhgk')
qhgk_cond_matrix = qhgk_cond.conductivity.sum(axis=0)
print('kappa from QHGK (W/mK) along x: %.3f'%(qhgk_cond_matrix[0, 0]))
print('kappa from QHGK (W/mK) along y: %.3f'%(qhgk_cond_matrix[1, 1]))
print('kappa from QHGK (W/mK) along z: %.3f'%(qhgk_cond_matrix[2, 2]))

if is_compute_full_QHGK:
    print('\n')
    inverse_cond_matrix = (Conductivity(phonons=phonons,method='inverse').conductivity.sum(axis=0))
    print('kappa from inverseion (W/mK) along x: %.3f' %(inverse_cond_matrix[0,0]))
    print('kappa from inverseion (W/mK) along y: %.3f' %(inverse_cond_matrix[1,1]))
    print('kappa from inverseion (W/mK) along z : %.3f' %(inverse_cond_matrix[2,2]))

print('\n')
rta_cond_matrix = (Conductivity(phonons=phonons, method='rta').conductivity.sum(axis=0))
print('kappa from RTA (W/mK) along x: %.3f'%(rta_cond_matrix[0, 0]))
print('kappa from RTA (W/mK) along y: %.3f'%(rta_cond_matrix[1, 1]))
print('kappa from RTA (W/mK) along z: %.3f'%(rta_cond_matrix[2, 2]))

if is_compute_full_QHGK:
    print('\n')
    print('kappa full QHGK (W/mK) along x: %.3f' %(qhgk_cond_matrix[0,0] - rta_cond_matrix[0,0]  + inverse_cond_matrix[0,0])) 
    print('kappa full QHGK (W/mK) along y: %.3f' %(qhgk_cond_matrix[1,1] - rta_cond_matrix[1,1]  + inverse_cond_matrix[1,1]))
    print('kappa full QHGK (W/mK) along z: %.3f' %(qhgk_cond_matrix[2,2] - rta_cond_matrix[2,2]  + inverse_cond_matrix[2,2]))
