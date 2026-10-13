# Example: wurtzite GaN, phonon dispersion without the non-analytic correction
# Computes: harmonic phonons; the polar LO-TO splitting is missing on purpose,
#           compare with phonon_with_NAC.py
# Uses: DFPT force constants from QE (q2r run without epsil, so the file
#       contains total force constants)

import numpy as np
from kaldo.forceconstants import ForceConstants
from kaldo.phonons import Phonons
import kaldo.controllers.plotter as plotter
import os

supercell = np.array([5, 5, 5])

force_constants = ForceConstants.from_folder(
    supercell=supercell,
    only_second=True,
    folder="fc_DFT",
    format="qe-d3q",
)

phonons_config = {
    "kpts": [9, 9, 9],
    "is_classic": False,
    "temperature": 300,
    "folder": "ALD_GaN_phonons_no_NAC",
    "storage": "formatted",
}
phonons = Phonons(forceconstants=force_constants, **phonons_config)

plotter.plot_dispersion(phonons, n_k_points=300, with_velocity=True, is_showing=False)
plotter.plot_dos(phonons, bandwidth=0.01, filename="dos")
os.rename("plots", "plots_no_NAC")
print("GaN phonons without the non-analytic correction done!")
