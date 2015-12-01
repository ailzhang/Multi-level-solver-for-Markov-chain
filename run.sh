#!/bin/bash

if [ -f ./GaussSeidel_log.txt ]
    then
    rm ./GaussSeidel_log.txt
fi 

if [ -f ./MultiLevel_log.txt ]
    then
    rm ./MultiLevel_log.txt
fi 

for i in $@
do
    python GaussSeidel.py $i >> GaussSeidel_log.txt
done

for i in $@
do
    python MultiLevel.py $i >> MultiLevel_log.txt
done

