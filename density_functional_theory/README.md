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

### List and content of examples folder
For each example, more detailed information is provided by the README.md file contained in the corresponding directory.
- `germanium_dft_d3q:`
This example illustrates how to perform thermal transport simulation for a germanium diamond (2 atoms per cell) with [D3Q](https://anharmonic.github.io/d3q/) package as force calculator.
- `magnesium_oxide_dft_d3q:`
This example illustrates how to perform thermal transport simulation for a rock-salt MgO (2 atoms per cell) system using [D3Q](https://anharmonic.github.io/d3q/) package as force calculator.
- `silicon_dft_qe:`
This example illustrates how to perform thermal transport simulation for a silicon diamond (2 atoms per cell) system using [QE](https://www.quantum-espresso.org/) package as force calculator.


---
### Git Large File Storage (LFS)

This repository uses Git LFS to handle large files. Ensure Git LFS is installed on your system by following the instructions on the [Git LFS website](https://git-lfs.github.com/).

Once installed, clone the repository as usual with `git clone` — large files will be downloaded automatically. If you've already cloned without Git LFS, retrieve the large files with:

```console
git lfs pull
```
