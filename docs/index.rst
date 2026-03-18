.. kALDo Examples documentation

.. image:: docsource/_resources/logo.png
   :width: 400

Examples
========

Understanding thermal transport in materials is crucial for applications ranging from thermoelectrics to thermal management in electronics. **Anharmonic lattice dynamics** captures the phonon-phonon interactions that govern heat conduction beyond the harmonic approximation.

This repository provides examples demonstrating how to use `kALDo <https://github.com/nanotheorygroup/kaldo>`_ to compute thermal conductivity using two complementary approaches:

- **Boltzmann Transport Equation (BTE)**: Solves for phonon populations under a temperature gradient, capturing both normal and Umklapp scattering processes.
- **Quasi-Harmonic Green-Kubo (QHGK)**: A unified approach that interpolates between the particle-like (BTE) and wave-like (Allen-Feldman) pictures of thermal transport.

The examples cover workflows with machine learning potentials, density functional theory (DFT), and empirical potentials.


.. toctree::
   :maxdepth: 2

   docsource/machine_learning_potentials/index
   docsource/density_functional_theory/index
   docsource/empirical_potentials/index


Contributing
------------

We welcome contributions from the community! If you have a thermal transport workflow using kALDo, whether with a new potential, a different material system, or an alternative method, we'd love to include it.

**How to contribute an example:**

1. Fork the repository and create a new branch
2. Add your example in the appropriate category folder (``machine_learning_potentials/``, ``density_functional_theory/``, or ``empirical_potentials/``)
3. Include a ``README.md`` describing the calculation and a Jupyter notebook (``.ipynb``) for visualization
4. Push your branch and open a Pull Request

The documentation is auto-generated from the example folders, so your example will automatically appear on the docs site once merged.

For questions or suggestions, feel free to `open an issue <https://github.com/nanotheorygroup/kaldo-examples/issues>`_.
