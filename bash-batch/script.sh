#!/bin/bash

#to activate this bash file: chmod +x script.sh

echo hello

echo temporary use of a proxy
export http_proxy=myproxy:8080
export https_proxy=myproxy:8080
#proxy will be used until CLI is exited
#note: DNF & APT-GET don't use global variable

source myotherscript

ls -a | grep whatImlookingfor

ssh user@host

scp -r sourcefolder user@host/destinationfolder


df -h /myfolder # disk usage -h = human readable
du --max-depth=1 --human-readable /var/lib/docker/overlay2 | sort --human-numeric-sort #list folder and size, sort by size
