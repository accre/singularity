#!/bin/bash

#SBATCH --mem=10G  # Total memory (RAM) required, per node
#SBATCH --time=0:03:00  # Wall Clock time (dd-hh:mm:ss) [max of 14 days]
#SBATCH --account=accre_gpu
#SBATCH --partition=maxwell     # low-latency RoCE network and 4 Titan X GPUs per node
#SBATCH --gres=gpu:2            # GPUs allocated

PORT_NUM=8888

echo "This job will run a Jupyter notebook from within a Singularity image"
echo "To view the notebook, create a new ssh connection to accre with port forwarding:"
echo "ssh -N -L 9999:$hostname:$PORTNUM $USER@login.accre.vanderbilt.edu"

setpkgs -a singularity

# To run a jupyter notebook
singularity run /scratch/singularity-images/tensorflow-1.0-jupyter-gpu.img $PORT_NUM


# To run a python script
#singularity exec /scratch/singularity-images/tensorflow-1.0-jupyter-gpu.img \
#  mytensorflowscript.py
