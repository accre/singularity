Bootstrap:docker  
From:ubuntu:18.04

%help
    A container for Hail program with current version number. One thing to note, that the jdk in version of 8 is necessary, jdk 11 does not work 

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
       wget \
		 cmake \
		 tar \
		 git \
		 python3 \
		 python3-pip \
		 liblapack3  \
       libopenblas-base \
		 libopenblas-dev \
		 liblapack-dev

    # now let's download the install the spark
    cd /tmp
    wget https://mirrors.gigenet.com/apache/spark/spark-2.4.6/spark-2.4.6-bin-hadoop2.7.tgz
    tar -xvf spark-2.4.6-bin-hadoop2.7.tgz
    mv spark-2.4.6-bin-hadoop2.7 /opt/spark

    # use pip install
    python3 -m pip install hail ipython PyVCF

    # post-setup script
    mkdir /scratch /data /gpfs52 /gpfs51 /gpfs23

%environment

    export PATH=/opt/spark/bin:$PATH
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

