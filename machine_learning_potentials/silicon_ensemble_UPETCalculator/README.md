### Phonon dispersion of silicon with ensemble uncertainty (PET-MAD + kaldo)

> Running `python phonon_uq.py` requires [UPET](https://github.com/lab-cosmo/upet)
> and [kaldo](https://github.com/nanotheorygroup/kaldo) (>= 2.2.1) to be installed.

- Execute `python phonon_uq.py` to compute the silicon phonon dispersion with an
  ensemble of independent PET-MAD models (XS and S) and report the mean and
  standard deviation of the phonon frequencies, using `kaldo.PhononsEnsemble`.

- The calculation proceeds as follows:
  - The Si diamond cell is relaxed with the XS model under `FixSymmetry`.
  - `PhononsEnsemble.from_calculators` runs a finite-difference second-order
    calculation per model, projects each set of force constants onto the
    space-group-invariant subspace (kaldo's force-constant symmetrization), and
    builds a `Phonons` per member.
  - `mean_std("frequency")` returns the mean and standard deviation of the phonon
    frequencies across the ensemble.

- This example uses a small set of independent models, which is a rougher
  uncertainty estimate than a calibrated committee. The full committee-based
  uncertainty quantification (e.g. 128 last-layer prediction-rigidity heads
  evaluated batched) is provided by
  [uqphonon](https://github.com/ppegolo/uqphonon) (Pegolo and Ceriotti). The
  uncertainty method follows shallow ensembles (Kellner and Ceriotti, 2024) and
  the last-layer prediction rigidity framework (Bigi et al., 2024). kaldo does not
  depend on those packages.
