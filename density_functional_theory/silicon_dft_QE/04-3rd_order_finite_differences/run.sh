#!/bin/bash
sed -i -e "s/startingpot = 'file'//g" BASE.scf_sc.in
sed -i -e "s/startingwfc = 'file'//g" BASE.scf_sc.in

mpirun -np 16 pw.x -inp BASE.scf_sc.in > BASE.scf_sc.out
cp -r tmp tmp-init

for file in DISP.scf_sc.in.*
do
    rm -r tmp
    cp -r tmp-init tmp
    
    outname="DISP.scf_sc.out.$(echo $file | cut -d '.' -f 4)"

    mpirun -np 16 pw.x -inp $file > $outname
done
