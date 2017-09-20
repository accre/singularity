#!/bin/bash
#
# This script performs a smart copy to /tmp to facilitate running Singularity images from /tmp.
# Specifically, this script checks to see if a file is present on /tmp and copies it there if it is not present. 
# It also uses file locking to ensure that only one process does the copy, rather than multiple processes, which
# could easily occur if a group of jobs are submitted at the same time (e.g. via job arrays).
#
# File locking method taken from: https://unix.stackexchange.com/questions/22044/correct-locking-in-shell-scripts
#
# Author: Will French, Advanced Computing Center for Research and Education (ACCRE), Vanderbilt University

[ $# -ne 3 ] && { echo "Usage: $0 sourcefile destfile lockfile"; exit 999; }

sourcefile=$1
destfile=$2
lockfile=$3

if ( set -o noclobber; echo "$$" > "$lockfile") 2> /dev/null; then

        trap 'rm -f "$lockfile"; exit $?' INT TERM EXIT

        # Perform the copy if: 
        # (1) the destination file does not exist OR
        # (2) the source and destination differ (via file size comparison)
        if [ ! -f "$destfile" ]
        then

                echo "$destfile does not exist."
                echo "Copying $sourcefile to $destfile"
                cp $sourcefile $destfile

        elif (( $(stat -c%s "$sourcefile") != $(stat -c%s "$destfile") ))
        then

                echo "$sourcefile and $destfile are NOT identical."
                echo "Copying $sourcefile to $destfile"
                cp $sourcefile $destfile

        else

                echo "$destfile already exists. Not copying anything."
                touch $destfile # update timestamp so file does not get purged from /tmp

        fi

        # clean up after yourself, and release your trap
        rm -f "$lockfile"
        trap - INT TERM EXIT

else

        echo "Lock Exists: $lockfile owned by $(cat $lockfile). I am not responsible for the copy."
        sleep 2 # sleep for a few seconds and then try to acquire the lock again
        bash $0 $@ # a process does not exit until it has acquired the lock at least once

fi
