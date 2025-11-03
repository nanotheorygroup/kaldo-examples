mpirun -np 16 pw.x < scf.in > scf.out
mpirun -np 16 ph.x < ph.in > ph.out
mpirun -np 16 q2r.x < q2r.in > q2r.out
