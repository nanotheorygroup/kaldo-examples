## Computing and Plotting 3rd-Order Thermal Properties for Ge bulk using kALDo:

> Running `thermal_conductivity.py` requires [ASE](https://ase-lib.org) and [kALDo](https://github.com/nanotheorygroup/kaldo) to be installed.  
> NOTE: Example uses **d3q ver. 1.1.10, QE ver. 7.2**

Perform BTE calculations using kALDo for Germanium. Like for the previous step, create a folder `fc_DFT/` and input the calculated `espresso.ifc2` and `FORCE_CONSTANTS_3RD` and the provided `CONTROL` file.

   - An example procedure for performing this calculation is below:

  ```console
     mkdir fc_DFT/
     cp CONTROL fc_DFT/
     cp ../01-2nd_order_DFPT/espresso.ifc2 fc_DFT/
     cp ../03-3rd_order_d3q/FORCE_CONSTANTS_3RD fc_DFT/
     python thermal_conductivity.py
  ```
  - After performing the calculation, use the Jupyter notebook `kALDo_with_d3q_gallery.ipynb` to visualize all properties calculated during simulation.
  -  Reference thermal conductivity for example (10x10x10 2nd order sc, 3x3x3 3rd order sc, 14x14x14 k-point mesh):
     - **55.2 W/m-K (Inversion), 44.4 W/m-K (Isotopic)**
