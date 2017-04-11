# tensorflow-1.0-jupyter-gpu

Creates a singularity container based on Ubuntu 16.10 that contains a GPU-enabled
version of TensorFlow and Jupyter notebooks. Recommended use is to develop 
the code in a Jupyter notebook, which can be launched via:

```bash
singularity run /scratch/singularity-images/tensorflow-1.0-jupyter-gpu.img <port_num>
```

and then run production-scale code using python 
scripts, e.g.:

```bash
singularity exec /scratch/singularity-images/tensorflow-1.0-jupyter-gpu.img \
  mytensorflowscript.py
```
