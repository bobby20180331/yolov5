#!/bin/bash 
echo "\n now killing kill train.py  \n usage: sh s2-kill.sh \n  "
project_home="/data/ai/yolov5"
# cd $project_home
filename="kill2021train"
 (ps -ef | grep train.py | awk '{print $2}' | xargs kill -9)> $filename 2>&1 &

sleep 1s 

echo "\n train.py was  killed success!" 
