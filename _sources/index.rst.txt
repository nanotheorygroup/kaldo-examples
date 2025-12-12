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


Machine Learning Potentials
---------------------------

Applications
^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   Cesium Lead Bromide Nep Tdep <docsource/machine_learning_potentials/cesium_lead_bromide_NEP_TDEP>
   Gallium Arsenide Orb V3 Orbcalculator <docsource/machine_learning_potentials/gallium_arsenide_orb-v3_ORBCalculator>
   Magnesium Oxide Mattersim V1 1M Mattersimcalculator <docsource/machine_learning_potentials/magnesium_oxide_MatterSim-v1-1M_mattersimcalculator>
   Silicon Mattersim V1 1M Mattersimcalculator <docsource/machine_learning_potentials/silicon_MatterSim-v1-1M_mattersimcalculator>
   Silicon Nep89 Calorine <docsource/machine_learning_potentials/silicon_NEP89_calorine>
   Silicon Carbide Mattersim V1 1M Mattersimcalculator <docsource/machine_learning_potentials/silicon_carbide_MatterSim-v1-1M_mattersimcalculator>
   Wurtzite Aluminum Nitride Ace Pyace <docsource/machine_learning_potentials/wurtzite_aluminum_nitride_ACE_PyACE>


These examples demonstrate kALDo workflows using **machine learning interatomic potentials (MLIPs)**. MLIPs combine near-DFT accuracy with the computational efficiency of classical potentials, enabling accurate thermal transport predictions at a fraction of the cost.


.. include:: ../machine_learning_potentials/README_details.md
   :parser: myst_parser.sphinx_


Density Functional Theory
-------------------------

Applications
^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   Germanium Dft D3Q <docsource/density_functional_theory/germanium_dft_d3q>
   Magnesium Oxide Dft D3Q <docsource/density_functional_theory/magnesium_oxide_dft_d3q>
   Silicon Dft Qe <docsource/density_functional_theory/silicon_dft_qe>


These examples demonstrate kALDo workflows using **density functional theory (DFT)** calculations. DFT provides highly accurate interatomic force constants from first principles, making it the gold standard for predicting thermal conductivity in crystalline materials. The workflows shown here use **Quantum ESPRESSO** for DFT calculations and **D3Q** or **thirdorder.py** for computing anharmonic (3rd order) force constants.


.. include:: ../density_functional_theory/README_details.md
   :parser: myst_parser.sphinx_


Empirical Potentials
--------------------

Applications
^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   Amorphous Silicon Tersoff Lammps <docsource/empirical_potentials/amorphous_silicon_Tersoff_LAMMPS>
   Carbon Diamond Tersoff Ase Lammps <docsource/empirical_potentials/carbon_diamond_Tersoff_ASE_LAMMPS>
   Carbon Nanotube Tersoff Lammps <docsource/empirical_potentials/carbon_nanotube_Tersoff_LAMMPS>
   Silicon Clathrate Tersoff Lammps <docsource/empirical_potentials/silicon_clathrate_Tersoff_LAMMPS>


These examples demonstrate kALDo workflows using **empirical interatomic potentials**. Classical potentials like Tersoff and Stillinger-Weber provide computationally efficient force evaluations, enabling thermal transport calculations for large systems and complex structures. The workflows shown here use **LAMMPS** and **ASE** for force constant calculations.


.. include:: ../empirical_potentials/README_details.md
   :parser: myst_parser.sphinx_
