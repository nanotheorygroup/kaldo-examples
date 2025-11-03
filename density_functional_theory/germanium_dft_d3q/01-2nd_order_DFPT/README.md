## Create 2nd-order Interatomic Force Constants for Ge bulk using Quantum Espresso.

> Additional Resources:  
> d3q: https://anharmonic.github.io/d3q/  
> Quantum Espresso (QE): https://www.quantum-espresso.org/

- Execute the `run-01.sh` script to run all necessary commands to obtain the 2nd order force constants `espresso.ifc2`.
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

- Once the initial IFC computations are done, you can rerun phonon calculations independently with different supercells.

- Note on Supercell Convergence:  
  The supercells used for espresso.ifc2 and FORCE_CONSTANTS_3RD are not necessarily at convergence. Adjust these as necessary based on your convergence criteria and the specifics of your calculation.
