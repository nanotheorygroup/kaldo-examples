# `argon_cumulant_LJ_TDEP`

Example argon_cumulant_LJ_TDEP illustrates how to compute anharmonic cumulant
corrections to the harmonic free energy of Lennard-Jones FCC argon (1 atom per
primitive cell) from TDEP force constants, using the `kaldo.cumulant`
subpackage. The one-atom primitive makes this the minimal-complexity cumulant
workflow.

External files required (vendored under `tdep_data/`, from a
[LatticeDynamicsToolkit.jl](https://github.com/ejmeitz/LatticeDynamicsToolkit.jl)
sTDEP run at 80 K):

1. tdep_data/infile.ucposcar: rhombohedral Ar primitive cell
2. tdep_data/infile.ssposcar: 4x4x4 cubic conventional supercell (non-diagonal tiling, det M = 256)
3. tdep_data/infile.forceconstant, infile.forceconstant_thirdorder, infile.forceconstant_fourthorder: IFC2/IFC3/IFC4

- cumulant_free_energy.py proceeds as follows:

    1. Load IFC2/IFC3/IFC4 with `ForceConstants.from_folder(supercell_matrix=M, format="tdep", include_fourth=True)`.

    2. Compute the quartic first-order cumulant F1 = <V_4>_0 with `F1_from_fc`.

    3. Compute the cubic second-order cumulant F2 = <V_3 V_3>_0 with `F2_from_fc`.

    4. Print F1/F2 on 3^3 and 5^3 q-meshes with the mesh-converged (8^3) reference.

No LAMMPS installation is needed: F1 and F2 are analytic sums over the force
constants.

Requires kaldo with the `kaldo.cumulant` subpackage
(nanotheorygroup/kaldo#283).
