"""
Cumulant free-energy corrections for Stillinger-Weber silicon at 100 K.

Demonstrates the canonical kaldo-native flow for computing the quartic
(F1) and cubic (F2) anharmonic cumulant corrections to the harmonic
free energy of a crystal, given a TDEP-format set of force constants.

The TDEP data under ``tdep_data/`` (IFC2/IFC3/IFC4 from a Stillinger-Weber
sTDEP run, originally from LatticeDynamicsToolkit.jl) is vendored so the
example runs without external dependencies. Replace the folder path with
your own TDEP run output to apply the same analysis to other materials.

Steps:
  1. Load IFC2/IFC3/IFC4 from the TDEP folder via
     ``ForceConstants.from_folder(supercell_matrix=M, include_fourth=True)``.
     The ``supercell_matrix`` kwarg is required when the ssposcar is a
     non-diagonal tiling of the primitive (e.g. rhombohedral primitive
     packed into a cubic conventional supercell). For diagonal tilings
     pass ``supercell=(N, N, N)`` instead.
  2. Compute F1 (quartic <V_4>_0 cumulant) via ``F1_from_fc``.
  3. Compute F2 (cubic <V_3 V_3>_0 cumulant) via ``F2_from_fc``.
  4. Print mesh-converged results against the Julia LDT reference.

Run::

    python cumulant_free_energy.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

from kaldo.forceconstants import ForceConstants
from kaldo.cumulant import F1_from_fc, F2_from_fc


TDEP_DATA = Path(__file__).parent / "tdep_data"

# Si diamond primitive in a 3x3x3 cubic conventional supercell:
# rhombohedral primitive (a/2, a/2, 0), (0, a/2, a/2), (a/2, 0, a/2)
# tiled into a 16.29-Angstrom cubic supercell.
SI_M = np.array([[3, -3, 3], [3, 3, -3], [-3, 3, 3]], dtype=int)
SI_MASS_AMU = 28.0855
TEMPERATURE_K = 100.0


def main():
    print(f"Loading TDEP IFCs from {TDEP_DATA}")
    fc = ForceConstants.from_folder(
        folder=str(TDEP_DATA),
        supercell_matrix=SI_M,
        format="tdep",
        include_fourth=True,
    )
    print(f"Loaded primitive: {len(fc.atoms)} atoms; "
          f"supercell: |det M| = {fc.n_replicas} replicas\n")

    masses_amu = np.full(len(fc.atoms), SI_MASS_AMU)
    print(f"{'mesh':>8s}  {'F1 (eV/atom)':>16s}  {'F2 (eV/atom)':>16s}")
    print("-" * 46)
    for n in (2, 3, 5):
        kmesh = (n, n, n)
        r1 = F1_from_fc(fc, masses_amu=masses_amu, kmesh=kmesh,
                        T_K=TEMPERATURE_K, use_q_symmetry=True)
        r2 = F2_from_fc(fc, masses_amu=masses_amu, kmesh=kmesh,
                        T_K=TEMPERATURE_K, sigma_THz=None,
                        use_q_symmetry=True)
        print(f"{n}^3       {r1['F1']:+16.5e}  {r2['F2']:+16.5e}")

    print("\nReference (Julia LDT):")
    print(f"{'mesh':>8s}  {'F1 (eV/atom)':>16s}  {'F2 (eV/atom)':>16s}")
    print("-" * 46)
    print(f"2^3       {+1.07160e-04:+16.5e}  {-2.29733e-05:+16.5e}")
    print(f"3^3       {+1.09492e-04:+16.5e}  {-2.43223e-05:+16.5e}")
    print(f"5^3       {+1.10129e-04:+16.5e}  {-2.48061e-05:+16.5e}")


if __name__ == "__main__":
    main()
