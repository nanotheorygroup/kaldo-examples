# Example: wurtzite GaN, phonon dispersion with the non-analytic correction
# Computes: harmonic phonons with LO-TO splitting from the Gonze correction
# Uses: DFPT force constants from QE (q2r run WITHOUT epsil, so the file
#       contains total force constants), Born charges supplied explicitly

import numpy as np
from kaldo.forceconstants import ForceConstants
from kaldo.phonons import Phonons
import kaldo.controllers.plotter as plotter
import os

# GaN is polar: the non-analytic correction needs the dielectric tensor and
# Born effective charges. These values are the AlmaBTE GaN_wurtzite reference
# set (BORN file); replace them with the values from your own DFPT run.
# Note the anisotropy between the in-plane and c-axis components.
EPSILON = np.diag([5.5429220, 5.5429220, 5.8492550])
Z_GA = np.diag([2.5749225, 2.5749225, 2.7477150])
Z_N = -Z_GA

supercell = np.array([5, 5, 5])

force_constants = ForceConstants.from_folder(
    supercell=supercell,
    only_second=True,
    folder="fc_DFT",
    format="qe-d3q",
)

# Attach the charge data: kALDo applies the Gonze non-analytic correction
# automatically whenever these are present.
atoms = force_constants.second.atoms
atoms.info["dielectric"] = EPSILON
atoms.set_array("charges", np.array([Z_GA, Z_GA, Z_N, Z_N]), shape=(3, 3))

phonons_config = {
    "kpts": [9, 9, 9],
    "is_classic": False,
    "temperature": 300,
    "folder": "ALD_GaN_phonons_with_NAC",
    "storage": "formatted",
}
phonons = Phonons(forceconstants=force_constants, **phonons_config)

plotter.plot_dispersion(phonons, n_k_points=300, with_velocity=True, is_showing=False)
plotter.plot_dos(phonons, bandwidth=0.01, filename="dos")
os.rename("plots", "plots_with_NAC")
print("GaN phonons with the non-analytic correction done!")
