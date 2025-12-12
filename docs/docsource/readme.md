# Overview

Understanding thermal transport in materials is crucial for applications ranging from thermoelectrics to thermal management in electronics. **Anharmonic lattice dynamics** captures the phonon-phonon interactions that govern heat conduction beyond the harmonic approximation.

This repository provides examples demonstrating how to use [**kALDo**](https://github.com/nanotheorygroup/kaldo) to compute thermal conductivity using two complementary approaches:

- **Boltzmann Transport Equation (BTE)**: Solves for phonon populations under a temperature gradient, capturing both normal and Umklapp scattering processes.
- **Quasi-Harmonic Green-Kubo (QHGK)**: A unified approach that interpolates between the particle-like (BTE) and wave-like (Allen-Feldman) pictures of thermal transport.

The examples cover workflows with density functional theory (DFT), empirical potentials, and machine learning potentials.
