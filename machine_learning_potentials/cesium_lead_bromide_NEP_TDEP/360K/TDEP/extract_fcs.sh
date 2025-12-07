#!/bin/sh

# Parse outputs from GPUMD trajectory outputs (tdep_fit_configurations.xyz)
tdep_parse_output --temperature 360 tdep_fit_configurations.xyz

# Don't proceed until parsing completes
wait

# Extract force constants using 4 porcessors with 18 angstrom cutoff from 2nd and 9 angstrom cutoff from 3rd force consnts
mpirun -np 4 extract_forceconstants --temperature 360 -rc2 18 -rc3 9 > extract_fcs.log

# Don't proceed unit fitting is completed
wait

# Rename outputs to input for kALDo
mv outfile.forceconstant infile.forceconstant
mv outfile.forceconstant_thirdorder infile.forceconstant_thirdorder
