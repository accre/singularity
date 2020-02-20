Bootstrap: docker
From: ezlabgva/busco:v4.0.4_cv1 

%help
    This recipe builds busco with currently latest version

%post

    # make the home and data folders from ACCRE available for this image
    # in this image the /data folder is already created, so we do not need it create the binding path
    mkdir /scratch /gpfs52 /gpfs23



