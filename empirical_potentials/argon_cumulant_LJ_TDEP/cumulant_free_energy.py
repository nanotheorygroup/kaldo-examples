"""
Cumulant free-energy corrections for Lennard-Jones argon at 80 K.

Demonstrates the cumulant flow on a centrosymmetric Lennard-Jones FCC
crystal. Argon has a one-atom primitive cell, so the multi-atom IFC3/IFC4
phase factors collapse: a useful "minimal-complexity" sanity case.

The TDEP data under ``tdep_data/`` (IFC2/IFC3/IFC4 from an LJ sTDEP run,
originally from LatticeDynamicsToolkit.jl) is vendored so the example runs
without external dependencies. Replace the folder path with your own TDEP
run output to apply the same analysis to other LJ-like atomic systems
(Ne, Kr, ...).

Run::

    python cumulant_free_energy.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

from kaldo.forceconstants import ForceConstants
from kaldo.cumulant import F1_from_fc, F2_from_fc


TDEP_DATA = Path(__file__).parent / "tdep_data"

# rhombohedral primitive in 4x4x4 cubic conventional supercell
AR_M = np.array([[4, -4, 4], [4, 4, -4], [-4, 4, 4]], dtype=int)
AR_MASS_AMU = 39.948
TEMPERATURE_K = 80.0


def main():
    print(f"Loading TDEP IFCs from {TDEP_DATA}")
    fc = ForceConstants.from_folder(
        folder=str(TDEP_DATA),
        supercell_matrix=AR_M,
        format="tdep",
        include_fourth=True,
    )
    print(f"Loaded primitive: {len(fc.atoms)} atom; "
          f"supercell: |det M| = {fc.n_replicas} replicas\n")

    masses_amu = np.full(1, AR_MASS_AMU)
    print(f"{'mesh':>8s}  {'F1 (eV/atom)':>16s}  {'F2 (eV/atom)':>16s}")
    print("-" * 46)
    for n in (3, 5):
        kmesh = (n, n, n)
        r1 = F1_from_fc(fc, masses_amu=masses_amu, kmesh=kmesh,
                        T_K=TEMPERATURE_K, use_q_symmetry=True)
        r2 = F2_from_fc(fc, masses_amu=masses_amu, kmesh=kmesh,
                        T_K=TEMPERATURE_K, sigma_THz=None,
                        use_q_symmetry=True)
        print(f"{n}^3       {r1['F1']:+16.5e}  {r2['F2']:+16.5e}")

    print()
    print("Mesh-converged (8^3): F1 = +1.011e-3, F2 = -4.788e-4 eV/atom")


if __name__ == "__main__":
    main()
