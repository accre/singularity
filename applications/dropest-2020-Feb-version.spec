Bootstrap: docker
From: vpetukhov/dropest:latest

%help
    This recipe builds dropest with currently latest version

%post

    # make the home and data folders from ACCRE available for this image
    mkdir /scratch /data /gpfs52 /gpfs23



