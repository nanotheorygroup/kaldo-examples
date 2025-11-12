## Create 3rd-order Interatomic Force Constants for MgO using Quantum Espresso and d3q.

> Additional Resources:  
> d3q: https://anharmonic.github.io/d3q/  
> Quantum Espresso (QE): https://www.quantum-espresso.org/

- Execute the following commands to obtain the 3rd order force constants `FORCE_CONSTANTS_3RD`.  
      
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
   `d3_qq2rr.x`: Obtains 3rd order force constants (`mat3R`) by translating matrices from reciprocal space into real space and recenters into a format to be used by kALDo (`FORCE_CONSTANTS_3RD`).
   ```console
   ls FILD3DYN/anh* | d3_qq2rr.x 3 3 3 -o mat3R > d3_qq2rr.out
   ls FILD3DYN/anh* | d3_qq2rr.x 3 3 3 -f 0 -o FORCE_CONSTANTS_3RD > kaldo_3ifc.out
   ```
   `d3_asr3.x`: Applies accoustic sum rules to 3rd order force constants to create `FORCE_CONSTANTS_3RD`.
   ```console
   d3_asr3.x -i FORCE_CONSTANTS_3RD -o FORCE_CONSTANTS_3RD.asr -t 1.e-12 -n 10000 -p 2 -m > d3_asr3.out
   ```
 
 - Since non-analytical correction (NAC) only applies to second order, only one modulus is needed for 3rd IFCs computation.

 - Once the initial IFC computations are done, you can rerun phonon calculations independently with different supercells.

- Note on Supercell Convergence:  
  The supercells used for FORCE_CONSTANTS_3RD are not necessarily at convergence. Adjust these as necessary based on your convergence criteria and the specifics of your calculation.
