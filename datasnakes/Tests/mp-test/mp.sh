# Author: Shaurita D. Hutchins
# Date Created: Tue Mar 28 18:29:14 2017
# Project Name: Addictions Project
# This is a simple bash script that gets GI lists for the local blast.

#PBS -S /bin/bash
#PBS -m bea
#PBS -M rgilmore@umc.edu
#PBS -l select=10:ncpus=1:mem=1gb -l place=free
#PBS -l cput=24:00:00
#PBS -l walltime=32:00:00
#PBS -N mptest
#PBS -o getgilists.o${PBS_JOBID}
#PBS -e getgilists.e${PBS_JOBID}
#PBS -j oe

cd ${PBS_O_WORKDIR}

mpiexec python child.py


