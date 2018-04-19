# TensorFlow 1.7 + Keras

## Building the container

To build the container, you need to install singularity ([linux](https://singularity.lbl.gov/install-linux)|[mac](https://singularity.lbl.gov/install-mac)|[windows](https://singularity.lbl.gov/install-linux)) and run the following commands:

```bash
sudo ./build.sh
```

In case you want to skip the testing - given you might not have all the required dependencies such as _CUDA 9_ and _cuDNN 7_: 

```bash
sudo singularity build --no-test tf-keras.img tensorflow-1.7-keras.def
```

## Transferring to ACCRE

The transfer of the image should be done using utilities like `rsync` or `ftp`. The generated file will be too large for tools like `scp` to be appropriate. 

## Running the container 

After requesting the node(s) required for the job, either interactively or as a batch job, the container must be given access to the _NVIDIA_ drivers in the cluster. After connecting to _ACCRE_, the following commands will run a file `test.py`:

```bash
ml GCC OpenMPI CUDA cuDNN Singularity
singularity exec --nv tf-keras.img python3 test.py
```