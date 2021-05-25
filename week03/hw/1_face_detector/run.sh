#!/bin/bash
#xhost +
#export DISPLAY=:0

#docker run -it --rm --device /dev/video0 --network host -e DISPLAY=$DISPLAY -v /tmp:/tmp sudhrity/facedetector:v1 
docker run -it --rm --device /dev/video0 --network host -e DISPLAY=$DISPLAY -v /tmp:/tmp sudhrity/facedetector:v1  bash
