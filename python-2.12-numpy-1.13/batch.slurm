#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --mem=1G  # Total memory (RAM) required, per node
#SBATCH --time=0:05:00  # Wall Clock time (dd-hh:mm:ss) [max of 14 days]

# Put the needed modules in your environment
module load GCC Singularity

# Run the container's test to ensure everything is behaving as expected
singularity test /scratch/singularity-images/python-2.12-numpy-1.13.img

# Process a Python file within the container
singularity run /scratch/singularity-images/python-2.12-numpy-1.13.img vectorization.py

