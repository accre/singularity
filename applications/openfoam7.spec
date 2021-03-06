Bootstrap: docker
From: centos:7

%help
    This recipe builds OpenFOAM-7.

%labels
    Author Fatih Ertinaz

%post
    ### Install prerequisites
    yum groupinstall -y 'Development Tools' 
    yum install -y openmpi3.x86_64 openmpi3-devel
    yum install -y wget git openssl-devel libuuid-devel

    ### Update environment
    export PATH=$PATH:/lib64/openmpi3/bin
    export CPATH=/usr/include/openmpi3-x86_64

    ### OpenFOAM version
    pkg=OpenFOAM
    vrs=7

    ### Install under $HOME/OpenFOAM -- will be changed to /opt
    mkdir -p /opt/$pkg
    cd /opt/$pkg

    ### Download OF
    wget -O - http://dl.openfoam.org/source/$vrs | tar xz
    mv $pkg-$vrs-version-$vrs $pkg-$vrs

    ### Download ThirdParty
    wget -O - http://dl.openfoam.org/third-party/$vrs | tar xz
    mv ThirdParty-$vrs-version-$vrs ThirdParty-$vrs

    ### Change dir to OpenFOAM-version
    cd $pkg-$vrs

    ### Get rid of unalias otherwise singularity fails
    sed -i 's/alias wmUnset/#alias wmUnset/' etc/config.sh/aliases
    sed -i '77s/else/#else/' etc/config.sh/aliases
    sed -i 's/unalias wmRefresh/#unalias wmRefresh/' etc/config.sh/aliases

    ### Source OF
    . etc/bashrc 

    ### Compile and install
    ./Allwmake 2>&1 | tee log.Allwmake

    ### Add sourcing to the .bashrc
    echo '. /opt/OpenFOAM/OpenFOAM-7/etc/bashrc' >> $SINGULARITY_ENVIRONMENT

    # make the home and data folders from ACCRE available for this image
    mkdir /scratch /data /gpfs52 /gpfs23

%environment
    export PATH=$PATH:/lib64/openmpi3/bin
    . /opt/OpenFOAM/OpenFOAM-7/etc/bashrc

%runscript
    icoFoam -help


