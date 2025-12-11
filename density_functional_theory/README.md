# density_functional_theory
This collection of examples shows how to perform thermal transport with kALDo for cystaline
systems using DFT. Before running simulations with kALDo, download the following third-party packages: [QE](https://www.quantum-espresso.org/), [D3Q](https://anharmonic.github.io/d3q/)

- Instructions of installing QE can be accessed [here](https://pranabdas.github.io/espresso/setup/install/)
- Suggestions of specificing GPU/CPU usage for tensorflow can be accessed [here](https://stackoverflow.com/questions/40069883/how-to-set-specific-gpu-in-tensorflow).

## List and content of examples folder
For each example, more detailed information is provided by the README.md file contained in the corresponding directory.
- `germanium_dft_d3q:`
This example illustrates how to perform thermal transport simulation for a germanium diamond (2 atoms per cell) with [D3Q](https://anharmonic.github.io/d3q/) package as force calculator.
- `magnesium_oxide_dft_d3q:`
This example illustrates how to perform thermal transport simulation for a rock-salt MgO (2 atoms per cell) system using [D3Q](https://anharmonic.github.io/d3q/) package as force calculator.
- `silicon_dft_qe:`
This example illustrates how to perform thermal transport simulation for a silicon diamond (2 atoms per cell) system using [QE](https://www.quantum-espresso.org/) package as force calculator.

## Using Git Large File Storage (LFS)

This repository uses Git Large File Storage (LFS) to handle large files. To ensure you properly download all the content, you may need to have Git LFS installed on your system. If you haven't installed it yet, you can do so by following the instructions on the [Git LFS website](https://git-lfs.github.com/). Once Git LFS is installed, you can clone this repository as usual with `git clone`. Git LFS is integrated into normal Git commands, so large files will be downloaded automatically when you checkout a commit that includes them. If you've already cloned the repository without Git LFS, you can download the large files with `git lfs pull`.
