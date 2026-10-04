"""Phonon dispersion of silicon with ensemble uncertainty using kaldo.

Builds a small committee of independent PET-MAD models (XS and S), computes the
phonon dispersion for each with kaldo, and reports the mean and standard deviation
of the phonon frequencies across the committee via kaldo.PhononsEnsemble.

This demonstrates the kaldo ensemble API with independent models. The full
calibrated committee (e.g. 128 last-layer prediction-rigidity heads evaluated
batched via i-PI) is available through uqphonon
(https://github.com/ppegolo/uqphonon); see the README.

Requires kaldo >= 2.2.0 (for PhononsEnsemble and force-constant symmetrization)
and UPET (https://github.com/lab-cosmo/upet).
"""
import numpy as np
import matplotlib.pyplot as plt
from ase.build import bulk
from ase.constraints import FixSymmetry
from ase.filters import StrainFilter
from ase.optimize import BFGS

from upet.calculator import UPETCalculator
from kaldo.ensemble import PhononsEnsemble
import kaldo.controllers.plotter as plotter

DEVICE = "cpu"
SUPERCELL = (3, 3, 3)
KPTS = (5, 5, 5)

# Independent committee members: the XS and S PET-MAD variants.
members = [
    UPETCalculator(model="pet-mad-xs", device=DEVICE, dtype="float32", version="1.5.0"),
    UPETCalculator(model="pet-mad-s", device=DEVICE, dtype="float32", version="1.5.0"),
]

# Relax with the first model, keeping the diamond cubic symmetry.
atoms = bulk("Si", "diamond", a=5.43)
atoms.calc = members[0]
atoms.set_constraint(FixSymmetry(atoms))
BFGS(StrainFilter(atoms), logfile=None).run(fmax=1e-4)
atoms.set_constraint(None)

# One finite-difference calculation per member, force constants symmetrized per
# member, then aggregated.
ensemble = PhononsEnsemble.from_calculators(
    atoms, SUPERCELL, members,
    delta_shift=3e-2, symmetrize=True,
    kpts=KPTS, temperature=300, storage="memory",
)

mean, std = ensemble.mean_std("frequency")
print("mean frequency shape:", mean.shape)
print("max frequency std over the k-point mesh (THz):", float(std.max()))

# Each ensemble member is an ordinary Phonons object, usable with any kaldo
# plotting or analysis. Here we save the dispersion of the first member.
plotter.plot_dispersion(ensemble.members[0], is_showing=False)
plt.savefig("dispersion_member0.png", dpi=150)
print("Saved dispersion_member0.png")
