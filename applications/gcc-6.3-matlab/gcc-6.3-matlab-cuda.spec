BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%labels
  Maintainer Fenglai Liu

%help
  This image is modified from a base container for ACCRE use with Lmod support,
  which originally developed by Eric
  Now we added the GCC 6.3 and cuda 10.1 to this image so that to support the 
  combination usage of CUDA+MATLAB+GCC.

%environment
  export MODULEPATH_ROOT=/accre/arch/easybuild/modules/all
  export MODULEPATH=$MODULEPATH_ROOT/Core:$MODULEPATH_ROOT/BinDist
  export LMOD_SHORT_TIME=86400
  export LMOD_ADMIN_FILE=/accre/common/lmod/etc/admin.lmod
  export LMOD_RC=/accre/common/lmod/etc/lmodrc.lua
  source /usr/local/lmod/lmod/init/bash

  # loading gcc
  export PATH=/opt/gcc/bin:/opt/gcc/libexec/gcc/x86_64-pc-linux-gnu/6.3.0:$PATH
  export LD_LIBRARY_PATH=/opt/gcc/lib64:/opt/gcc/lib/gcc/x86_64-pc-linux-gnu/6.3.0:$LD_LIBRARY_PATH

  # loading GCC libraries 
  export LD_LIBRARY_PATH=/opt/gmp/lib:/opt/mpfr/lib:/opt/mpc/lib:$LD_LIBRARY_PATH

  # loading cuda stuff
  export PATH=/usr/local/cuda/bin:$PATH
  export LD_LIBRARY_PATH=usr/local/cuda/lib64:$LD_LIBRARY_PATH

%setup
  install -Dv \
    accre_lmod_bash_profile \
    ${SINGULARITY_ROOTFS}/etc/profile.d/accre_01_lmod.sh

%post

  # basic 
  yum -y install epel-release
  yum -y install wget bzip2 gcc tcl tk tar procps git zlib-devel 

  # all of the building stuff
  yum -y install autoconf automake binutils bison flex gcc gcc-c++ gettext libtool make patch pkgconfig

  # install kernel head and other related things
  # this is needed for the cuda 
  yum -y install kernel-devel.x86_64 kernel-headers.x86_64
  yum -y install dkms

  # now let's download cuda and install it
  # make sure to change the CUDA version etc. if you need another version
  cd /tmp
  CUDA="cuda-repo-rhel7-10.0.130-1.x86_64.rpm"
  wget https://developer.download.nvidia.com/compute/cuda/repos/rhel7/x86_64/${CUDA}
  rpm --install ${CUDA}
  yum clean expire-cache
  yum list --showduplicates cuda
#  yum list --showduplicates cuda-drivers
#  yum list --showduplicates nvidia-driver-latest-dkms
  yum -y install nvidia-driver-latest-dkms cuda-drivers cuda-10.0.130-1.x86_64

  # gmp
  cd /opt
  wget ftp://gcc.gnu.org/pub/gcc/infrastructure/gmp-4.3.2.tar.bz2
  bunzip2 gmp-4.3.2.tar.bz2
  tar xvf gmp-4.3.2.tar
  cd gmp-4.3.2
  ./configure --prefix=/opt/gmp
  make  
  make install
  export LD_LIBRARY_PATH=/opt/gmp/lib:$LD_LIBRARY_PATH

  # mpfr
  cd /opt
  wget ftp://gcc.gnu.org/pub/gcc/infrastructure/mpfr-2.4.2.tar.bz2
  bunzip2 mpfr-2.4.2.tar.bz2
  tar xvf mpfr-2.4.2.tar
  cd mpfr-2.4.2
  ./configure --prefix=/opt/mpfr --with-gmp=/opt/gmp
  make && make install
  export LD_LIBRARY_PATH=/opt/mpfr/lib:$LD_LIBRARY_PATH

  # mpc
  cd /opt
  wget ftp://gcc.gnu.org/pub/gcc/infrastructure/mpc-0.8.1.tar.gz
  tar zxvf mpc-0.8.1.tar.gz
  cd mpc-0.8.1
  ./configure --prefix=/opt/mpc --with-gmp=/opt/gmp --with-mpfr=/opt/mpfr
  make && make install
  export LD_LIBRARY_PATH=/opt/mpc/lib:$LD_LIBRARY_PATH

  # install gcc 6.3
  cd /opt
  wget http://ftpmirror.gnu.org/gcc/gcc-6.3.0/gcc-6.3.0.tar.bz2 
  tar -xvf gcc-6.3.0.tar.bz2
  cd gcc-6.3.0
  mkdir build && cd build
  ../configure                                         \
	  --prefix=/opt/gcc                                    \
	  --disable-multilib                               \
	  --with-system-zlib                               \
	  --with-gmp=/opt/gmp                               \
	  --with-mpfr=/opt/mpfr                               \
	  --with-mpc=/opt/mpc                               \
	  --enable-languages=c,c++,fortran 
  make && make install

  # Install Lmod
  cd /tmp
  export LMOD_VERSION=8.1.7
  yum -y install http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
  yum -y install lua lua-filesystem lua-posix lua-term lua-devel
  wget https://github.com/TACC/Lmod/archive/${LMOD_VERSION}.tar.gz
  tar xzf ${LMOD_VERSION}.tar.gz
  cd Lmod-${LMOD_VERSION}
  ./configure --with-spiderCacheDir=/accre/arch/lmod/cache \
              --with-updateSystemFn=/accre/arch/lmod/cache/timestamp.lmod \
              --with-tcl=no
  make install
  cd ..
  rm -rf ${LMOD_VERSION}.tar.gz Lmod-${LMOD_VERSION}

  # Setup CVMFS binds for ACCRE software stack
  mkdir -p /accre /cvmfs

