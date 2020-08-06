Bootstrap:docker  
From:ubuntu:20.04

%labels
  Maintainer Fenglai Liu

%help
  Base container for internal ACCRE use with Lmod support
  To access the software stack make sure to bind mount /accre and /cvmfs
  This one is modified from Eric yum spec file

%environment
  export MODULEPATH_ROOT=/accre/arch/easybuild/modules/all
  export MODULEPATH=$MODULEPATH_ROOT/Core:$MODULEPATH_ROOT/BinDist
  export LMOD_SHORT_TIME=86400
  export LMOD_ADMIN_FILE=/accre/common/lmod/etc/admin.lmod
  export LMOD_RC=/accre/common/lmod/etc/lmodrc.lua
  #source /usr/local/lmod/lmod/init/bash

%post
  # download the packages for base system
  apt-get update && apt-get install -y wget bzip2 gcc tcl tk tar git procps make

  # install the lua5.2 
  apt-get install -y  lua5.2  liblua5.2-0  liblua5.2-dev lua-term  lua-filesystem  lua-posix 

  # Setup CVMFS binds for ACCRE software stack
  mkdir -p /accre /cvmfs

  # post-setup for ACCRE dirs
  # these are the binding path
  mkdir /scratch /data /dors /gpfs51  /gpfs52 /gpfs23
