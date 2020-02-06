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
		 cmake \
       libhdf5-mpi-dev  \
		 gcc-4.7 \
		 gfortran-4.7 \
		 openmpi-bin \
       pax-utils  \
		 tar \
		 git \
       postgresql \
       libpq-dev \
       liblapack3 \
       libblas3  


    # post-setup script
    mkdir /scratch /data /gpfs52 /gpfs23

%environment
    
    # set up the PATH
    PATH=/usr/local/bin:$PATH

    # get rid of the warning when each time launch the singularity 
	 export LC_ALL=C.UTF-8
	 export LANG=C.UTF-8
	 echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
	 echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

