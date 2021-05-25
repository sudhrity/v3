#!/bin/bash

kubectl delete deployment facedetector
kubectl apply -f facedetector.yaml
