
#!/bin/bash

#docker build --no-cache -t face_detector -f Dockerfile .
docker build --no-cache  -t sudhrity/facedetector:v1 -f Dockerfile .
