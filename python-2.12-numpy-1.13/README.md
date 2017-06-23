# python-2.12-numpy-1.13

Creates a singularity container based on Ubuntu 16.10 that includes Python 2.12 
and NumPy 2.13. Many of the other common python packages for scientific computing (SciPy,
Matplotlib, Pandas, Scikit-learn, etc) are also installed.

Load the latest version of Singularity using Lmod:

```bash
module load GCC Singularity
```

The following command will enable you to allow you to run a python script within 
the container. In this example, we are running the ```vectorization.py``` file 
within the container.

```bash
singularity run /scratch/singularity-images/python-2.12-numpy-1.13 vectorization.py
```

You might also wish to run the NumPy unit tests within the container to verify that
everything is working as expected. 

```bash
singularity test /scratch/singularity-images/python-2.12-numpy-1.13
```

