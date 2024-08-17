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

show_help()
{
    echo ""
    echo "  extract_needed_files.sh [-g|r]"
    echo "      options:"
    echo "      g     get all the installs/drivers"
    echo "      r     clean all the installs"
    echo ""
}

get_installs()
{
    echo "Getting installs"

    # Pull down CUDA install
    if [[ ! -d "$ABS_PATH_CUDA_EXTRACT" ]]; then
        [[ ! -f "$CUDA_NAME" ]] && curl -O "$CUDA_URL" || echo "Already Exists: $CUDA_NAME"
        mkdir -p "$CUDA_NAME"
        sh "./$CUDA_NAME.run" --extract="${ABS_PATH_CUDA_EXTRACT}"
    else
        echo "Already Exists: $ABS_PATH_CUDA_EXTRACT"
    fi

    # CUDNN install
    [[ ! -f "$NV_CUDNN_FILE" ]] && curl -O "$NV_CUDNN_URL" || echo "Already Exists: $NV_CUDNN_FILE" &

    # DRIVER
    [[ ! -f "$NV_DRIVER_FILE" ]] && curl -O "$NVIDIA_DRIVER_URL" || echo "Already Exists: $NV_DRIVER_FILE" &

    # # Extracts the file into NVIDIA-Linux-x86_64-535.129.03
    [[ ! -d "$NVIDIA_DRIVER_FOLDER" ]] && sh "./$NV_DRIVER_FILE" --extract-only || echo "Already Exists: $NVIDIA_DRIVER_FOLDER" &

}

clean_installs()
{
    printf "Removing the files/directories\n\n"

    [[ -f "$NV_CUDA_FILE" ]] && rm "$NV_CUDA_FILE" && echo "$NV_CUDA_FILE deleted"
    [[ -f "$NV_CUDNN_FILE" ]] && rm "$NV_CUDNN_FILE" && echo "$NV_CUDNN_FILE deleted"
    [[ -f "$NV_DRIVER_FILE" ]] && rm "$NV_DRIVER_FILE" && echo "$NV_DRIVER_FILE deleted"
    [[ -d "$CUDA_NAME" ]] && rm -rf "$CUDA_NAME" && echo "$CUDA_NAME deleted"
    [[ -d "$NVIDIA_DRIVER_FOLDER" ]] && rm -rf "$NVIDIA_DRIVER_FOLDER" && echo "$NVIDIA_DRIVER_FOLDER deleted"
    [[ -d "$ABS_PATH_CUDA_EXTRACT" ]] && rm -rf "$ABS_PATH_CUDA_EXTRACT" && echo "$ABS_PATH_CUDA_EXTRACT deleted"
}

getopts "gr" o

# while getopts "gr" o; do
case "${o}" in
    "g")
        get_installs;;
    "r")
        clean_installs;;
    "?")
        show_help
        ;;
esac  
# done



