Bootstrap:docker  
From:ubuntu:20.04

%labels
  Maintainer Fenglai Liu

%help
  Base container for internal ACCRE use with Lmod support
  To access the software stack make sure to bind mount /accre and /cvmfs
  This one is modified from Eric yum spec file

%setup
  install -Dv \
    accre_lmod_bash_profile \
    ${SINGULARITY_ROOTFS}/etc/profile.d/accre_01_lmod.sh

%environment
  export MODULEPATH_ROOT=/accre/arch/easybuild/modules/all
  export MODULEPATH=$MODULEPATH_ROOT/Core:$MODULEPATH_ROOT/BinDist
  export LMOD_SHORT_TIME=86400
  export LMOD_ADMIN_FILE=/accre/common/lmod/etc/admin.lmod
  export LMOD_RC=/accre/common/lmod/etc/lmodrc.lua

%runscript
  sh -c ". /usr/local/lmod/lmod/init/sh"

%post

  # set up the timezone
  export TZ=America/Chicago
  ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

  # download the packages for base system
  apt-get update && apt-get install -y build-essential wget bzip2 gcc tcl tk tar git procps make

  # install the lua5.2 
  apt-get install -y  lua5.1  liblua5.1-0  liblua5.1-dev lua-term  lua-filesystem  lua-posix 

  # Install Lmod
  export LMOD_VERSION=8.1.7
  cd /tmp
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

  # post-setup for ACCRE dirs
  # these are the binding path
  mkdir -p /scratch /data /dors /gpfs51 /gpfs52 /gpfs23
