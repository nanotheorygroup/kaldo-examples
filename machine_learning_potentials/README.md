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

### GPU/CPU Configuration

For TensorFlow-based calculations, you can specify GPU or CPU usage following [these instructions](https://stackoverflow.com/questions/40069883/how-to-set-specific-gpu-in-tensorflow).

---

### Git Large File Storage (LFS)

This repository uses Git LFS to handle large files. Ensure Git LFS is installed on your system by following the instructions on the [Git LFS website](https://git-lfs.github.com/).

Once installed, clone the repository as usual with `git clone` — large files will be downloaded automatically. If you've already cloned without Git LFS, retrieve the large files with:

```console
git lfs pull
