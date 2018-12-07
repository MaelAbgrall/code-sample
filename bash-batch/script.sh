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
