#!/usr/bin/bash

NV_DRIVER_VERSION="535.104.05"
NVIDIA_VERSION="12.2.2"
# CUDA
CUDA_NAME="cuda_${NVIDIA_VERSION}_${NV_DRIVER_VERSION}_linux"
NV_CUDA_FILE="${CUDA_NAME}.run"
CUDA_URL="https://developer.download.nvidia.com/compute/cuda/${NVIDIA_VERSION}/local_installers/$NV_CUDA_FILE"
ABS_PATH_CUDA_EXTRACT="$(realpath "./${CUDA_NAME}")"
# CUDNN
NV_CUDNN_FILE="cudnn-linux-x86_64-9.3.0.75_cuda12-archive.tar.xz"
NV_CUDNN_URL="https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-x86_64/${NV_CUDNN_FILE}"
# NVIDIA driver
NVIDIA_DRIVER_FOLDER="NVIDIA-Linux-x86_64-${NV_DRIVER_VERSION}"
NV_DRIVER_FILE="$NVIDIA_DRIVER_FOLDER.run"
NVIDIA_DRIVER_URL="https://us.download.nvidia.com/tesla/${NV_DRIVER_VERSION}/${NV_DRIVER_FILE}"

# Pull down CUDA install
if [[ ! -d "$ABS_PATH_CUDA_EXTRACT"]]; then
    [[ ! -f "$CUDA_NAME" ]] && curl -O "$CUDA_URL"
    mkdir -p "$CUDA_NAME"
    sh "./$CUDA_NAME.run" --extract="${ABS_PATH_CUDA_EXTRACT}"
fi

# CUDNN install
[[ ! -f "$NV_CUDNN_FILE" ]] && curl -O "$NV_CUDNN_URL"

# DRIVER
[[ ! -f "$NV_DRIVER_FILE" ]] && curl -O "$NVIDIA_DRIVER_URL"

# # Extracts the file into NVIDIA-Linux-x86_64-535.129.03
# [[ ! -d "$NVIDIA_DRIVER_FOLDER" ]] && sh ./NVIDIA-Linux-x86_64-535.129.03.run --extract-only

