Bootstrap:docker  
From:ubuntu:18.04

%help
    A container for Hail program, in version of 0.2.49. One thing to note, that the jdk in version of 8 is necessary, jdk 11 does not work 

%labels 
    Author Fenglai liu (fenglai@accre.vanderbilt.edu)

%post
    
    # download the packages for base system
    apt-get update && apt-get install -y \
       openjdk-8-jre-headless  \
		 openjdk-8-jdk-headless  \
		 build-essential \
       gfortran \
       g++ \
       autoconf  \
		 cmake \
		 tar \
		 git \
		 python3 \
		 python3-pip \
		 liblapack3  \
       libopenblas-base \
		 libopenblas-dev \
		 liblapack-dev

    # use pip install
    python3 -m pip install hail ipython PyVCF

    # post-setup script
    mkdir /scratch /data /gpfs52 /gpfs51 /gpfs23

%environment
    
