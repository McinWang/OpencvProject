import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# Read the image to fill the detection box area (Optional)
# img = cv2.imread('.jpg')
# Read the face part of the image (required manual setting)
# mbg = img[150:400,200:450]

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    flag, frame = cap.read()
    frame= cv2.flip(frame,1)

    if not flag:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3 ,5)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        # Optional setting
        #face = frame[y:y+h, x:x+w]
        #face = face[::10,::10]
        #face = cv2.resize(face, (30, 30))
        # mask
        #face = cv2.resize(face, (h, w))
        # cover face
        #face = cv2.resize(mbg, (h, w))
        #frame[y:y+h, x:x+w] = face

    cv2.imshow('faces Detected!',frame)
    key = cv2.waitKey(1000//24)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()