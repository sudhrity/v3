# this is from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
import cv2
import paho.mqtt.client as mqtt 
import pickle
import time

#LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="face_detector_topic"

# Create callback functions
def on_connect_local(client, userdata, flags, rc):
    print("Connected to local broker with rc: " + str(rc))

def on_publish_local(client, userdata, result):
    print("Data publlished")

# Create mqtt client
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.on_publish = on_publish_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)


# Create Face detector
face_clf = cv2.CascadeClassifier("/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml")


# Connect to camers. 
# The index depends on your camera setup and which one is your USB camera.
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    # # stop display cv2.imshow('frame', gray)

    # Detect face
    faces = face_clf.detectMultiScale(gray, 1.3, 5)


    for(x, y, w, h) in faces:

        print(faces)
        
        # Extract face 
        cropped_faces = gray[y:y+h, x:x+h]
        # stop display cv2.imshow('crop', cropped_faces)

        # Encode and publish 
        ret, png = cv2.imencode('.png', cropped_faces) 
        message = pickle.dumps(png)
        local_mqttclient.publish(LOCAL_MQTT_TOPIC, message, qos=0, retain=False)


    # Stop capture
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
