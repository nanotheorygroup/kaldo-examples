# Wurtzite GaN: phonon dispersion with the non-analytic correction

GaN is a polar semiconductor: without the non-analytic correction (NAC) the
longitudinal optical branch is degenerate with the transverse branches at the
zone center, and the dispersion is qualitatively wrong. This example computes
the harmonic phonons of wurtzite GaN twice from the same DFPT force constants
and shows the LO-TO splitting appear when Born charges are supplied
(at Gamma: TO 19.78 THz, LO 21.22 THz with the reference charges below).

Contents:

- `fc_DFT/`: second-order force constants (`espresso.ifc2`, 5x5x5) and the
  unit cell (`POSCAR`).
- `phonon.py`: dispersion and DOS without NAC (`plots_no_NAC/`).
- `phonon_with_NAC.py`: the same with the Gonze NAC (`plots_with_NAC/`).

Notes:

- kALDo applies the Gonze correction automatically whenever
  `atoms.info["dielectric"]` and `atoms.arrays["charges"]` are present.
- The force constants must be **total** force constants: run `q2r.x` without
  `epsil` (the flag line in `espresso.ifc2` reads `F`). Files produced with
  `epsil = .true.` embed the charges but store dipole-subtracted constants,
  a convention kALDo currently refuses with an explanatory error.
- The dielectric tensor and Born charges here are the AlmaBTE `GaN_wurtzite`
  reference values; replace them with the values from your own DFPT run
  (`ph.x` with `epsil = .true.` prints them; only copy them into the script,
  do not pass them to `q2r.x`).
