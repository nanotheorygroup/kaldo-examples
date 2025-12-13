# kALDo Examples

Official repository demonstrating various examples to use [kALDo](https://github.com/nanotheorygroup/kaldo) for thermal transport calculations.

<p align="center">
<img src="kaldo-schema.png" width="450">
</p>

## Overview

This repository provides examples demonstrating how to compute thermal conductivity using kALDo with two complementary approaches:

- **Boltzmann Transport Equation (BTE)**: Solves for phonon populations under a temperature gradient
- **Quasi-Harmonic Green-Kubo (QHGK)**: A unified approach interpolating between particle-like and wave-like thermal transport

The examples cover workflows with:

- **Machine Learning Potentials** (orb, NEP, MatterSim, ACE)
- **Density Functional Theory** (Quantum ESPRESSO, D3Q)
- **Empirical Potentials** (LAMMPS, Tersoff)
- **Finite Temperature Effective Potentials** (TDEP)

## Building the Documentation

### Requirements

```bash
pip install sphinx sphinx-immaterial nbsphinx myst-parser
```

### Build

```bash
cd docs
make html
```

The documentation will be generated in `docs/_build/html/`.
