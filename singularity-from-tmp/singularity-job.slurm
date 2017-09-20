#!/bin/bash
#SBATCH --mem=5G
#SBATCH --array=0-20
#SBATCH --output=%A_%a.out
###SBATCH --partition=debug

image=python-2.12-numpy-1.13.img

src=/scratch/singularity-images/${image}
dest=/tmp/${image} # this should be on /tmp

# This is the file lock that is unique to each node. Alternatively, it could
# be stored on /tmp of each node. This file will be cleaned up automatically
# UNLESS a copy fails (e.g. due to exceeding a job's memory allocation). If a copy
# fails, you should delete the lock file manually before launching more jobs.
lock=/scratch/${USER}/mylock.$(hostname) # each node should have its own lock

bash smart-tmp-copy.sh ${src} ${dest} ${lock}

module load GCC Singularity # Load default GCC and Singularity

singularity run ${dest} vectorization.py # Run image tests

# Do not clean up, in case other jobs of this kind land on this node in 
# the near future. 