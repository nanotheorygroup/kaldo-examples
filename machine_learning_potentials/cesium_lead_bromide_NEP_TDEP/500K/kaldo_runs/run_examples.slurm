#!/bin/bash
#SBATCH -A m5411
#SBATCH -C gpu
#SBATCH -q premium
#SBATCH -t 48:00:00
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1
#SBATCH -J kCsPbBr3-360K
# --------------------------------------------------------------#

# Lanuch run script
python thermal_conductivity.py 
