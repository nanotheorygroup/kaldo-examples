## Computing and Plotting 2nd-Order Thermal Properties for MgO bulk using kALDo:

> Running `phonon.py` requires [ASE](https://ase-lib.org) and [kALDo](https://github.com/nanotheorygroup/kaldo) to be installed.  
> NOTE: Example uses **d3q ver. 1.1.10, QE ver. 7.2**

- Perform lattice dynamic calculations with kALDo using the python script `phonon.py` to visualize data calculated from the 2nd order force constants.  
- To perform the calculation, make a folder `fc_DFT/` and move `espresso.ifc2` from the previous step, as well as the provided `POSCAR` structure file into this directory. Run `python phonon.py` for the calculation.
   - An example procedure for performing this calculation is below:
    
     ```console
     mkdir fc_DFT/
     cp POSCAR fc_DFT/
     cp ../02-2nd_order_DFPT/espresso.ifc2 fc_DFT/
     python phonon.py
     ```

     or

     ```console
     tar xzvf fc_DFT.tar.gz
     python phonon.py
     ```
     
- After performing the calculation, use the Jupyter notebook `phonon_plotter.ipynb` to plot phonon bands (dispersion relation).
