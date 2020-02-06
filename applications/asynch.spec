Bootstrap:docker  
From:ubuntu:18.04

%help
    A container for ASYNCH program. 

%labels 
    Author Fenglai liu (fenglai@accre.vanderbilt.edu)

%post
    
    # download the packages for base system
    echo "let's install the necessary components for the asynch program"
    apt-get update && apt-get install -y \
		 manpages-dev \
		 build-essential \
       gfortran \
       autoconf  \
		 cmake \
		 hdf5-tools \
       libhdf5-dev  \
       libhdf5-mpi-dev  \
		 openmpi-bin \
       pax-utils  \
		 tar \
		 git \
       postgresql \
       libpq-dev \
       pkg-config \
       liblapack3 \
       libblas3  

    # download the code
    SRC=/opt/asynch_2.0
    cd /opt
    git clone  https://github.com/Iowa-Flood-Center/asynch
    mv asynch asynch_2.0
    cd $SRC
    git checkout develop

    # begin compile
    cd $SRC && autoreconf --install 
    mkdir build && cd build
    ../configure CFLAGS="-O3 -DNDEBUG -Wno-format-security" --prefix=/opt/asynch
    make
    make install

    # post-setup script
    mkdir /scratch /data /gpfs52 /gpfs23

%environment
    
    # set up the PATH
    PATH=/opt/asynch/bin:$PATH

    # get rid of the warning when each time launch the singularity 
	 export LC_ALL=C.UTF-8
	 export LANG=C.UTF-8
	 echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
	 echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

