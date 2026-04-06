# `carbon_diamond_PTBP`

The example `carbon_diamond_PTBP` illustrates how to perform thermal transport simulations for a carbon
diamond (2 atoms per cell) system using [ASE and DFTB+](https://wiki.fysik.dtu.dk/ase/ase/calculators/dftb.html) as a force calculator
with the [PTBP parametrization](https://doi.org/10.1021/acs.jctc.4c00228).

External files required:
               1). PTBP Slater-Koster files (`C-C.skf`) from [Zenodo (DOI: 10.5281/zenodo.14289468)](https://zenodo.org/records/14289468)

- To set up DFTB+, install via conda-forge:

```console
conda install -c conda-forge dftbplus
```

- Download the PTBP parameter set from the Zenodo link above. Extract `C-C.skf` from `ptbp.zip/complete_set/` and place it in a directory. Set the `DFTB_PREFIX` environment variable:

```console
export DFTB_PREFIX=/path/to/ptbp_skf/
```

-   `1_harmonic.py`: Compute 2nd order force constants and harmonic properties
    (phonon dispersion, density of states, group velocity). This step is fast (minutes).

-   `2_anharmonic.py`: Compute 3rd order force constants, then calculate scattering
    rates and thermal conductivity using RTA. The 3rd order calculation is the slow
    step (~12 hours for a 3x3x3 supercell).

- To run this example, navigate to this directory and execute:

```console
# Step 1: 2nd order force constants and harmonic properties (fast)
python 1_harmonic.py

# Step 2: 3rd order force constants and thermal conductivity (slow)
python 2_anharmonic.py
```

- To view figures generated during simulations, navigate to this folder: `plots/11_11_11/`
- To access data computed during simulations, navigate to this folder: `ALD_c_diamond/`

## Convergence note

The thermal conductivity from this example (~31 W/m-K with RTA) is highly unconverged.
The experimental value for diamond is ~2200 W/m-K. The discrepancy comes from:

- **Supercell size**: A 3x3x3 supercell (54 atoms) is too small for converged third-order
  force constants in diamond. Larger supercells (5x5x5) are needed for convergence.
- **k-point mesh**: An 11x11x11 mesh may not be dense enough for full convergence.
- **DFTB+ accuracy**: DFTB is a semi-empirical method. The PTBP parametrization provides
  good structural and electronic properties across the periodic table, but anharmonic
  quantities can deviate significantly from DFT or experiment.

This example is intended as a starting point for using DFTB+ with kALDo, not as a
production-quality calculation.

## References

- PTBP parametrization: Cui, M., Reuter, K., & Margraf, J. T.,
  *J. Chem. Theory Comput.* (2024).
  [DOI: 10.1021/acs.jctc.4c00228](https://doi.org/10.1021/acs.jctc.4c00228)
- DFTB+: Hourahine, B. et al., *J. Chem. Phys.* 152, 124101 (2020).
  [DOI: 10.1063/1.5143190](https://doi.org/10.1063/1.5143190)
