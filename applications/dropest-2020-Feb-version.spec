Bootstrap: docker
From: vpetukhov/dropest:latest

%help
    This recipe builds dropest with currently latest version

%post

    # make the home and data folders from ACCRE available for this image
    mkdir /scratch /data /gpfs52 /gpfs23

    # we need to change the /home/user folder so that to have run permission for all of users
    chmod 755 /home/user



