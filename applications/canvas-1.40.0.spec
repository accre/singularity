Bootstrap:docker  
From:ubuntu:18.04

%help
    A container for Canvas program. 

%labels 
    Author Fenglai liu (fenglai@accre.vanderbilt.edu)

%post
    
    # download the packages for base system
    echo "let's install the necessary components for the Canvas program"
	 apt-get update
    apt-get install -y wget
    wget -q https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
	 dpkg -i packages-microsoft-prod.deb
    apt-get install -y software-properties-common
    add-apt-repository universe
	 apt-get update
	 apt-get install -y apt-transport-https  \
		 dotnet-sdk-3.1 \
       aspnetcore-runtime-3.1 \
       dotnet-runtime-3.1  \
		 mono-complete

    # install the canvas
    mkdir /opt/canvas
    cd /tmp
    wget https://github.com/Illumina/canvas/releases/download/1.40.0.1613%2Bmaster/Canvas-1.40.0.1613.master_x64.tar.gz
    tar -xvf Canvas-1.40.0.1613.master_x64.tar.gz
    mv Canvas-1.40.0.1613+master_x64/* /opt/canvas
    cd /opt/canvas
    chmod a+x tabix.exe
    chmod a+x tabix
    chmod a+x bedGraphToBigWig

    # post-setup script
    mkdir /scratch /data /gpfs52 /gpfs23

%environment
    
    # set up the PATH
    PATH=/opt/canvas:$PATH

    # get rid of the warning when each time launch the singularity 
	 export LC_ALL=C.UTF-8
	 export LANG=C.UTF-8
	 echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
	 echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

