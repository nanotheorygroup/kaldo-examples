# Compute kappa of Silicon with Quantum Espresso (QE)

> Input data descriptions for each executable in Quantum Espresso (QE) can be found [here](https://www.quantum-espresso.org/documentation/input-data-description/)

0. Setup the input file for QE. Please check out the official documents and various resources for this step. 
1. Preliminary step: Perform vc-relax in QE to relax the structures. After finishing the calculation of vc-relax, run `python3 export-POSCAR.py` (requires [ASE](https://wiki.fysik.dtu.dk/ase/)) to generate `POSCAR`. 
2. Perform DFPT calculations for 2nd order force constants `espresso.ifc2`. Please follow instructions in `02-2nd_order_DFPT` folder. 
3. Perform lattice dynamic calculations using [kALDo](https://github.com/nanotheorygroup/kaldo) script in the `03-kALDo_runs_phonon` folder and access the quality of 2nd order force constants. To perform the calculation, make a directory `fc_DFT` and copy the calculated results  `POSCAR` and `espresso.ifc2` from previous steps into this directory. Run `python phonon.py` for lattice dynamic calculation. See `phonon.py` for a detailed description. Here is a script to describe this step: 

```console
cd 03-kALDo_runs_phonon/
mkdir fc_DFT/
cp ../01-vcrelax/POSCAR fc_DFT/
cp ../02-2nd_order_DFPT/espresso.ifc2 fc_DFT/
python phonon.py
```

After finish this step, you can run the Jupyter notebook `phonon_plotter.ipynb` to plot phonon bands (dispersion relation). 

4. Perform finite-difference calculations for 3rd order force constants. Please follow instructions in the `04-3rd_order_finite_differences` folder.
5. Perform BTE calculations using [kALDo](https://github.com/nanotheorygroup/kaldo) in the `05-kALDo_runs_BTE` folder. Like in the previous step, create a directory `fc_DFT` and copy `POSCAR`, `espresso.ifc2` and `FORCE_CONSTANTS_3RD_D3Q` into it. Then run `python thermal_conductivity.py` to calculate. See `thermal_conductivity.py` for a detailed description. Here is a script to describe this step: 

```console
cd 05-kALDo_runs_BTE/
cp -r ../03-kALDo_runs_phonon/fc_DFT .
cp ../04-3rd_order_finite_differences/FORCE_CONSTANTS_3RD_D3Q fc_DFT/
python thermal_conductivity.py
```
After finish this step, you can run the Jupyter notebook `kALDo_with_QE_gallery.ipynb` for various properties. 

 Reference thermal conductivity for example (8x8x8 2nd order supercell, 3x3x3 3rd order supercell, 14x14x14 k-point mesh):
 - **146.0 W/m-K (Inversion), 133.1 W/m-K (Isotopic)**
