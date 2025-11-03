#!/bin/bash
module load  some/modules/for/qe 
export OMP_NUM_THREADS=8
echo $OMP_NUM_THREADS
echo " Done."

echo started at "$(date)"

bin="path/to/qe/bin"
pref="mpirun -np 12 "  # e.g. "mpirun -np 4 "
post="-npool 4 "  # e.g. -npool 4

echo "pw calculation"
$pref  $bin/pw.x $post -in pw.in > pw.out 

echo "ph calculation"
$pref $bin/ph.x $post -in ph.in > ph.out 

echo "computing 2-body force constants"
$pref $bin/d3_q2r.x < q2r.in > d3_q2r.out

echo "computing 2-body force constants for kaldo"
$pref $bin/q2r.x -in kaldo_q2r.in > kaldo_q2r.out

echo finished at "$(date)"

echo " Done."
