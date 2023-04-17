BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%labels
  Maintainer Prasanna Koirala

%help
  This image is modified from a base container for ACCRE use with Lmod support,
  which originally developed by Eric

%environment
  export MODULEPATH_ROOT=/accre/arch/easybuild/modules/all
  export MODULEPATH=$MODULEPATH_ROOT/Core:$MODULEPATH_ROOT/BinDist
  export LMOD_SHORT_TIME=86400
  export LMOD_ADMIN_FILE=/accre/common/lmod/etc/admin.lmod
  export LMOD_RC=/accre/common/lmod/etc/lmodrc.lua
  source /usr/local/lmod/lmod/init/bash

%setup

  install -Dv \
    accre_lmod_bash_profile \
    ${SINGULARITY_ROOTFS}/etc/profile.d/accre_01_lmod.sh

%files
  # copy files here

%post
    # yum needs some tlc to work properly in container
    RELEASEVER=7
    ARCH=x86_64
    echo $RELEASEVER > /etc/yum/vars/releasever
    echo $ARCH > /etc/yum/vars/arch
    
    rpm -ivh --nodeps http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    yum -d 10 check-update

    # basic 
    yum clean all
    yum -y install wget bzip2 gcc tcl tk tar procps git zlib-devel 

    # all of the building stuff
    yum -y install autoconf automake binutils bison flex gcc gcc-c++ gettext libtool make patch pkgconfig

    # matlab stuff
    yum -y install libXt libXext
 
    # Install Lmod
    cd /tmp
    export LMOD_VERSION=8.1.7
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

    mkdir /scratch /data /gpfs22 /gpfs23

    # Setup CVMFS binds for ACCRE software stack
    mkdir -p /accre /cvmfs
