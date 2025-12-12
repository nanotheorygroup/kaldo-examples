# Density Functional Theory

These examples demonstrate kALDo workflows using **density functional theory (DFT)** calculations. DFT provides highly accurate interatomic force constants from first principles, making it the gold standard for predicting thermal conductivity in crystalline materials. The workflows shown here use **Quantum ESPRESSO** for DFT calculations and **D3Q** or **thirdorder.py** for computing anharmonic (3rd order) force constants.

---

### Setup Instructions

### Requirements

Before running these examples, install the following packages:

- [Quantum ESPRESSO](https://www.quantum-espresso.org/) — Installation guide available [here](https://pranabdas.github.io/espresso/setup/install/)
- [D3Q](https://anharmonic.github.io/d3q/) — For computing anharmonic force constants

### GPU/CPU Configuration

For TensorFlow-based calculations, you can specify GPU or CPU usage following [these instructions](https://stackoverflow.com/questions/40069883/how-to-set-specific-gpu-in-tensorflow).

---

### Git Large File Storage (LFS)

This repository uses Git LFS to handle large files. Ensure Git LFS is installed on your system by following the instructions on the [Git LFS website](https://git-lfs.github.com/).

Once installed, clone the repository as usual with `git clone` — large files will be downloaded automatically. If you've already cloned without Git LFS, retrieve the large files with:

```console
git lfs pull
```
