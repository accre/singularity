Bootstrap: docker
From: vpetukhov/dropest:latest

%help
    This recipe builds dropest with currently latest version

%files
    dropest_r_packages.R /tmp

%post

    # install the missing R libraries
    echo "install the necessary R libraries"
    Rscript /tmp/dropest_r_packages.R

    # make the home and data folders from ACCRE available for this image
    mkdir /scratch /data /gpfs52 /gpfs23

    # we need to change the /home/user folder so that to have run permission for all of users
    chmod 755 /home/user



