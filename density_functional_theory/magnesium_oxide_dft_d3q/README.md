# Computing Thermal Conductivity of MgO with and w/o NAC:
  
>Input data descriptions for each executable in Quantum Espresso (QE) can be found [here](https://www.quantum-espresso.org).  
> Additional information regarding the use of d3q can be found [here](https://anharmonic.github.io/d3q).  
> Running `phonon.py`, `phonon_with_NAC.py`, `thermal_conductivity.py`, and `thermal_conductivity_with_NAC.py` requires [ASE](https://ase-lib.org) and [kALDo](https://github.com/nanotheorygroup/kaldo) to be installed.  
> NOTE: Examples use **d3q ver. 1.1.10, QE ver. 7.2**

  
0. Setup the required input files listed here: `pw.in`, `ph.in`, `q2r.in`, `scf.in`, `CONTROL`, `d3.in`, and the `UPF/` pseudopotential folder in their respective folders. Check out the documentation of QE and d3q for more information on this step.
   > Note: To fix the calculation with non-analytical correction (NAC), ensure the `ph.in` file includes the following setting:
   ```console
   epsil = .true.
   ```

1. Under `01-2nd_order_DFPT_with_NAC/`: Execute all necessary commands to obtain the 2nd order force constants `espresso.ifc2` with non-analytical correction (NAC).
   - Ensure the required input files are in the directory: `pw.in`, `ph.in`, `q2r.in`, `kaldo_q2r.in`, and the `UPF/` pseudopotential folder.
   
   `pw.x`: Performs self consistent field calculations for magnesium oxide.  
   ```console
   pw.x -in pw.in > pw.out
   ```
   `ph.x`: Calculates dynamical matrices on q-vector in reciprocal space for 2nd order.
   ```console
   ph.x -in ph.in > ph.out
   ```
   `d2r.x`: Obtains 2nd order force constants in a format to be used by kALDo (`espresso.ifc2`).  
   ```console
   q2r.x -in q2r.in > q2r.out
   ```

2. Under `02-2nd_order_DFPT/`: Execute all necessary commands to obtain the 2nd order force constants `espresso.ifc2` without non-analytical correction (NAC).
   - Ensure the required input files are in the directory: `scf.in`, `ph.in`, `q2r.in`, and the `UPF/` pseudopotential folder.
   
   `pw.x`: Performs self consistent field calculations for magnesium oxide.  
   ```console
   pw.x -in scf.in > scf.out
   ```
   `ph.x`: Calculates dynamical matrices on q-vector in reciprocal space for 2nd order.  
   ```console
   ph.x -in ph.in > ph.out
   ```
   `d2r.x`: Obtains 2nd order force constants in a format to be used by kALDo (`espresso.ifc2`).  
   ```console
   q2r.x -in q2r.in > q2r.out
   ```

3. Under `03-3rd_order_d3q/`: Execute all neccessary commands to obtain the 3rd order force constants `FORCE_CONSTANTS_3RD_D3Q`.
   - Ensure the required input files are in the directory: `scf.in`, `ph_for_d3q.in`, and the `UPF/` pseudopotential folder.

     `pw.x`: Performs self consistent field calculations for magnesium oxide.  
     ```console
     pw.x -in scf.in > scf.out
     ```
     `ph.x`: Calculates dynamical matrices on q-vector in reciprocal space for 2nd order.  
     ```console
     ph.x -in ph_for_d3q.in > ph_for_d3q.out
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
 
   - Since non-analytical correction (NAC) only applies to second order, only one modulus is needed for 3rd IFCs computation.

4. Under `04-kaldo_runs_BTE/`: Perform BTE calculations using kALDo for magnesium oxide with and without NAC.
   - Create two folders labeled `kaldo_runs_with_NAC/` and `kaldo_runs_without_NAC/`. In each respective folder, create another folder labeled `fc_DFT_with_NAC/` or `fc_DFT_withouth_NAC/`.
   - Move the calculated IFCs from the previous steps, along with the provided `POSCAR` file, into their respective `fc_DFT_with_NAC/` or `fc_DFT_withouth_NAC/` folders.
   - Alternatively, extract the provided input files from the `fc_DFT_with_NAC.tar.gz` or `fc_DFT.tar.gz`

   - An example of the procedure for performing this step is below:
     ```console
     cd 04-kaldo_runs_BTE/
     mkdir kaldo_runs_with_NAC/
     mkdir kaldo_runs_without_NAC/
     ```
   - Then:
     ```console
     cd kaldo_runs_without_NAC/
     mkdir fc_DFT/
     cp ../../02-2nd_order_DFPT/espressoifc2 fc_DFT/
     cp ../../03_3rd_order_d3q/FORCE_CONSTANTS_3RD_D3Q fc_DFT/
     cp POSCAR fc_DFT/
     python thermal_conductivity.py

     cd ../..

     cd kaldo_runs_with_NAC/
     mkdir fc_DFT_with_NAC/
     cp ../../01-2nd_order_DFPT_with_NAC/espresso.ifc2 fc_DFT_with_NAC/
     cp ../../03_3rd_order_d3q/FORCE_CONSTANTS_3RD_D3Q fc_DFT_with_NAC/
     cp POSCAR fc_DFT_with_NAC/
     python thermal_conductivity_with_NAC.py
     ```
   - Or:
     ```console
     cd kaldo_runs_without_NAC/
     tar xzvf fc_DFT.tar.gz
     python thermal_conductivity.py

     cd ../..

     cd kaldo_runs_with_NAC/
     tar xzvf fc_DFT.tar.gz
     python thermal_conductivity_with_NAC.py
     ```
     
   - After performing the calculations, run the Jupyter notebooks `kALDo_with_d3q_gallery_with_NAC.ipynb` and `kALDo_with_d3q_gallery_without_NAC.ipynb` to visualize all properties.
  
 - Reference thermal conductivity for examples:
   - With inclusion of NAC: **46.9 W/m-K** , **36.8 W/m-K with Isotopic Scattering**
   - Without inclusion of NAC: **52.9 W/m-K** , **41.2 W/m-K with Isotopic Scattering**
