# Singularity from /tmp

We have encountered slow downs when running several hundred singularity jobs simultaneously that
are all reading the same image from GPFS. See this GitHub issue for more details:

https://github.com/singularityware/singularity/issues/627

This example uses a bash script to facilitate copying the image to /tmp and running from that image instead.

*smart-tmp-copy.sh* first checks to see if an image is present in /tmp. If not, a single process copies it 
from GPFS. Linux file locking is employed to avoid multiple processes attempting to copy the image to /tmp
simultaneously. If the image is already on /tmp, the script also verifies that the image sizes are consistent. If
not, the local copy is overwritten with the version from GPFS. This allows updated versions of the images to
be easily deployed without updating the name of the image itself.