# Machine Learning Potentials

These examples demonstrate kALDo workflows using **machine learning interatomic potentials (MLIPs)**. MLIPs combine near-DFT accuracy with the computational efficiency of classical potentials, enabling accurate thermal transport predictions at a fraction of the cost.

---

### Setup Instructions

### Requirements

Before running these examples, install the following packages:

- MatterSim — Installation guide available [here](https://github.com/microsoft/mattersim)
- Orb - Installation guide available [here](https://github.com/orbital-materials/orb-models)
- TDEP - Installation guide available [here](https://tdep-developers.github.io/tdep/)
- pyACE - Installation guide available [here](https://github.com/ICAMS/python-ace)
- calorine - Instllation guide available [here](https://calorine.materialsmodeling.org/)
- pet-mad - Installation guide available [here](https://github.com/lab-cosmo/pet-mad)
----

## List and content of examples folder
For each example, more detailed information is provided by the README.md file contained in the corresponding directory.
- `cesium_lead_bromide_NEP_TDEP:`
This example illustrates how to perform thermal transport simulation for a cubic cesium lead bromide system (5 atom per cell) with [TDEP](https://tdep-developers.github.io/tdep/) and [GPUMD](https://gpumd.org/) packages as force calculator.
- `gallium_arsenide_orb-v3_ORBCalculator:`
This example illustrates how to perform thermal transport simulation for a gallium arsenide (2 atoms per cell) system using [Orb](https://github.com/orbital-materials/orb-model) package as force calculator.
- `magnesium_oxide_MatterSim-v1-1M_mattersimcalculator:`
This example illustrates how to model thermal expansion coefficients for a magnesium oxide (2 atoms per cell) system using [MatterSim](https://github.com/microsoft/mattersim) package as force calculator.
- `silicon_MatterSim-v1-1M_mattersimcalculator:`
This example illustrates how model thermal expansion coefficients for a silicon diamond (2 atoms per cell) system using [MatterSim](https://docs.lammps.org/Packages_details.html#pkg-phonon) package as force calculator.
- `silicon_NEP89_calorine:`
This example illustrates how to perform thermal transport simulation for a silicon diamond system (2 atom per cell) with [calorine](https://calorine.materialsmodeling.org/) packages as force calculator.
- `silicon_carbide_MatterSim-v1-1M_mattersimcalculator:`
This example illustrates how to perform thermal transport simulation for a silicon carbide system (2 atom per cell) with [MatterSim](https://github.com/microsoft/mattersim) packages as force calculator.
- `wurtzite_aluminum_nitride_ACE_PyACE:`
This example illustrates how to perform thermal transport simulation for an aluminum nitride system (4 atom per cell) with [pyACE](https://github.com/ICAMS/python-ace) packages as force calculator.
- `sodium_chloride_PETMADCalculator:`
This example illustrates how to perform thermal transport simulation for a sodium chloride system (2 atom per cell) with [PET-MAD](https://github.com/lab-cosmo/pet-mad) packages as force calculator.


---


### GPU/CPU Configuration

For TensorFlow-based calculations, you can specify GPU or CPU usage following [these instructions](https://stackoverflow.com/questions/40069883/how-to-set-specific-gpu-in-tensorflow).

---

### Git Large File Storage (LFS)

This repository uses Git LFS to handle large files. Ensure Git LFS is installed on your system by following the instructions on the [Git LFS website](https://git-lfs.github.com/).

Once installed, clone the repository as usual with `git clone` — large files will be downloaded automatically. If you've already cloned without Git LFS, retrieve the large files with:

```console
git lfs pull
