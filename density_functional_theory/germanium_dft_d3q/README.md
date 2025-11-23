# Computing Thermal Conductivity of Germanium with d3q:
  
>Input data descriptions for each executable in Quantum Espresso (QE) can be found [here](https://www.quantum-espresso.org).  
> Additional information regarding the use of d3q can be found [here](https://anharmonic.github.io/d3q).  
> Running `phonon.py` and `thermal_conductivity.py` requires [ASE](https://ase-lib.org) and [kALDo](https://github.com/nanotheorygroup/kaldo) to be installed.  
> NOTE: Example uses **d3q ver. 1.1.10, QE ver. 7.2**
  
0. Setup the required input files listed here: `pw.in`, `ph.in`, `q2r.in`, `kaldo_q2r.in`, `CONTROL`, `d3.in`, and the `UPF/` pseudopotential folder in their respective folders. Check out the documentation of QE and d3q for more information on this step.  
1. Under `01-2nd_order_DFPT/`: Execute all necessary commands to obtain the 2nd order force constants `espresso.ifc2`.
   - Ensure the required input files are in the directory: `pw.in`, `ph.in`, `q2r.in`, `kaldo_q2r.in`, and the `UPF/` pseudopotential folder.
   
      `pw.x`: Performs self consistent field calculations for Germanium.  
       ```console
       pw.x -in pw.in > pw.out
       ```
      `ph.x`: Calculates dynamical matrices on q-vector in reciprocal space for 2nd order.  
       ```console
       ph.x -in ph.in > ph.out
       ```
      `d3_q2r.x`: Obtains 2nd order force constants (`mat2R`) by translating matrices from reciprocal space into real space.  
       ```console
       d3_q2r.x < q2r.in > d3_q2r.out
       ```
      `d2r.x`: Obtains 2nd order force constants in a format to be used by kALDo (`espresso.ifc2`).  
       ```console
       q2r.x -in kaldo_q2r.in > kaldo_q2r.out
       ```
       
2. Under `02-kaldo_runs_phonon/`: Perform lattice dynamic calculations with kALDo using the python script `phonon.py` to visualize data calculated from the 2nd order force constants. To perform the calculation, make a folder `fc_DFT/` and move `espresso.ifc2` from the previous step, as well as the provided `CONTROL` structure file into this directory. Run `python phonon.py` for the calculation.
   - An example procedure for performing this calculation is below:
    
     ```console
     cd 02-kALDo_runs_phonon/
     mkdir fc_DFT/
     cp CONTROL fc_DFT/
     cp ../01-2nd_order_DFPT/espresso.ifc2 fc_DFT/
     python phonon.py
     ```
     
   - After performing the calculation, use the Jupyter notebook `phonon_plotter.ipynb` to plot phonon bands (dispersion relation).

3. Under `03-3rd_order_d3q/`: Execute all neccessary commands to obtain the 3rd order force constants `FORCE_CONSTANTS_3RD_D3Q`. This requires the `FILDRHO/` folder created from `ph.x` in step 1.

   ```console
   cp -r 01-2nd_order_DFPT/FILDRHO 03-3rd_order_d3q/
   ```
   
   - Ensure the input file `d3.in` is in the directory.
   
   `d3q.x`: Calculates dynamical matrices on q-vector in reciprocal space for 3rd order.
   ```console
   d3q.x -in d3.in > d3.out
   ```
   `d3_qq2rr.x`: Obtains 3rd order force constants (`mat3R`) by translating matrices from reciprocal space into real space and recenters into a format to be used by kALDo (`FORCE_CONSTANTS_3RD_D3Q`).
   ```console
   ls FILD3DYN/anh* | d3_qq2rr.x 3 3 3 -o mat3R > d3_qq2rr.out
   ls FILD3DYN/anh* | d3_qq2rr.x 3 3 3 -f 0 -o FORCE_CONSTANTS_3RD_D3Q > kaldo_3ifc.out
   ```
   `d3_asr3.x`: Applies accoustic sum rules to 3rd order force constants to create `FORCE_CONSTANTS_3RD_D3Q`.
   ```console
   d3_asr3.x -i FORCE_CONSTANTS_3RD_D3Q -o FORCE_CONSTANTS_3RD_D3Q.asr -t 1.e-12 -n 10000 -p 2 -m > d3_asr3.out
   ```

4. Under `04-kaldo_runs_BTE`: Perform BTE calculations using kALDo for Germanium. Like for the previous step, create a folder `fc_DFT/` and input the calculated `espresso.ifc2` and `FORCE_CONSTANTS_3RD_D3Q` and the provided `CONTROL` file.

   - An example procedure for performing this calculation is below:

    ```console
     cd 04-kALDo_runs_BTE/
     mkdir fc_DFT/
     cp CONTROL fc_DFT/
     cp ../01-2nd_order_DFPT/espresso.ifc2 fc_DFT/
     cp ../03-3rd_order_d3q/FORCE_CONSTANTS_3RD_D3Q fc_DFT/
     python thermal_conductivity.py
     ```

    - After performing the calculation, use the Jupyter notebook `kALDo_with_d3q_gallery.ipynb` to visualize all properties.
  
  Reference thermal conductivity for example (10x10x10 2nd order supercell, 3x3x3 3rd order supercell, 14x14x14 k-point mesh):
 - **55.2 W/m-K (Inversion), 44.4 W/m-K (Isotopic)**
