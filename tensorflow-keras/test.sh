#!/bin/bash
# Build and test with the system's nvidia drivers
singularity build --no-test tf-keras.img tensorflow-1.7-keras.def
singularity exec --nv tf-keras.img python3 -c 'import tensorflow as tf; tf.Session()'