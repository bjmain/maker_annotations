#!/bin/bash

# options for sbatch
#SBATCH --nodes=1
#SBATCH --time=6800
#SBATCH --mem=10G # Memory pool for all cores (see also --mem-per-cpu)
#SBATCH --partition=bml
#SBATCH --job-name="maker1"

# for calculating the amount of time the job takes
begin=`date +%s`
echo $HOSTNAME

# setting up variables
#sample=$1
#R1=${sample}_L006_R1_001.fastq.gz
#R2=${sample}_L006_R2_001.fastq.gz

# loading modules
module load maker

# running commands
cd /home/path_to/chnk_1
maker


# useGrid=False just runs the job locally within the resources I allocated and doesn't spawn other jobs on the farm. 
# finished commands

# getting end time to calculate time elapsed
end=`date +%s`
elapsed=`expr $end - $begin`
echo Time taken: $elapsed

