# `silicon_cumulant_SW_TDEP`

Example silicon_cumulant_SW_TDEP illustrates how to compute anharmonic cumulant
corrections to the harmonic free energy of crystalline silicon (2 atoms per
primitive cell) from Stillinger-Weber TDEP force constants, using the
`kaldo.cumulant` subpackage.

External files required (vendored under `tdep_data/`, from a
[LatticeDynamicsToolkit.jl](https://github.com/ejmeitz/LatticeDynamicsToolkit.jl)
sTDEP run at 100 K):

1. tdep_data/infile.ucposcar: rhombohedral Si primitive cell
2. tdep_data/infile.ssposcar: 3x3x3 cubic conventional supercell (non-diagonal tiling, det M = 108)
3. tdep_data/infile.forceconstant, infile.forceconstant_thirdorder, infile.forceconstant_fourthorder: IFC2/IFC3/IFC4

- cumulant_free_energy.py proceeds as follows:

    1. Load IFC2/IFC3/IFC4 with `ForceConstants.from_folder(supercell_matrix=M, format="tdep", include_fourth=True)`.
       The non-diagonal supercell is handled through kaldo's SNF replica mapping.

    2. Compute the quartic first-order cumulant F1 = <V_4>_0 with `F1_from_fc`.

    3. Compute the cubic second-order cumulant F2 = <V_3 V_3>_0 with `F2_from_fc`.

    4. Print F1/F2 on 2^3, 3^3, 5^3 q-meshes next to the Julia LatticeDynamicsToolkit reference values
       (agreement to <0.1% at every mesh).

No LAMMPS installation is needed: F1 and F2 are analytic sums over the force
constants. The companion Monte-Carlo constant correction (F_0), which does
require a LAMMPS single-point calculator, is exposed by
`kaldo.cumulant.cumulant_thermo`.

Requires kaldo with the `kaldo.cumulant` subpackage
(nanotheorygroup/kaldo#283).
