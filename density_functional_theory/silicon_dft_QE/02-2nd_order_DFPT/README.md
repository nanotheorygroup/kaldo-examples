# Compute 2nd order force constants with DFPT 

Perform self-consistent field calculations
        
```console
pw.x -inp scf.in > scf.out
```

Calculate dynamical matrices on q-vector in reciprocal space

```console
ph.x -inp ph.in > ph.out
```


Obtain second order interatomic force constants in the real space (Fourier transform of the output from the second step)

```console
q2r.x -inp q2r.in > q2r.out
```

We provided a script `runph.sh` for this step. 

