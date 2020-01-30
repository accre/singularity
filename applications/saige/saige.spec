Bootstrap:docker  
From:ubuntu:16.04

%help
    A container for SAIGE program. This container uses the current version of saige.

%labels 
    Author Fenglai liu (fenglai@accre.vanderbilt.edu)

%files
    install_packages.R  /opt

%post
    
    # download the packages for base system
    echo "let's install the necessary components for the saige program"
    apt-get update && apt-get install -y \
		 apt-transport-https \
		 build-essential \
		 cmake \
		 curl \
		 libboost-all-dev \
		 python-pip \
		 software-properties-common \
		 tar \
		 git \
       zlib1g  \
       zlib1g-dev \
		 libcurl3 \
       libpng12-0  \
       libreadline6 \
       liblzma5  \
       libpango-1.0-0  \
       libpangocairo-1.0-0  \
       liblapack3 \
       libblas3  \
       sqlite3  \
       zstd

    # adding the R
    echo "adding the R base"
	 apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 
	 add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu xenial-cran35/' 
	 apt-get update && apt-get install -y r-base r-base-core r-recommended

    # install the necessary R libraries
    echo "install the necessary R libraries"
    Rscript /opt/install_packages.R

    # install the cget 
	 echo "installing the cget"
	 pip install cget

    # now let's grap the saige repo
	 echo "downloading the saige git repo"
    cd /opt
    git clone --depth 1 https://github.com/weizhouUMICH/SAIGE.git
    SRC=/opt/SAIGE

    # all of the dependent libraries and head files are already placed in the configure
    cd $SRC
    ./configure

    # clear all of object files
    rm ${SRC}/src/*.o 
    rm ${SRC}/src/*.so

    # now we should go to install the saige
    R CMD INSTALL --build $SRC

    # post-setup script
    mkdir /scratch /data /gpfs52 /gpfs23

%environment
    
    # set up the PATH
    PATH=/usr/local/bin:$PATH

