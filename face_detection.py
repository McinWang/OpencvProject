# 读取一张图像，对图像中的人脸进行检测，将检测到的人脸框出

import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# 读取图像填充检测框区域
# img = cv2.imread('.jpg')
# 读取图像的人脸部分
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
        #face = frame[y:y+h, x:x+w]
        #face = face[::10,::10]
        #face = cv2.resize(face, (30, 30))
        # 图像框打马赛克
        #face = cv2.resize(face, (h, w))

        #face = cv2.resize(mbg, (h, w))
        #frame[y:y+h, x:x+w] = face

    cv2.imshow('faces Detected!',frame)
    key = cv2.waitKey(1000//24)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()





# # 读取图片
# img = cv2.imread('test4.jpg')
# # 转换为灰度图
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # 读取图片的宽和高
# height, width = gray.shape

# # 对图像中的人脸进行检测
# face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
# faces = face_cascade.detectMultiScale(gray, 1.3, 5)


# # 框出检测到的人脸
# for (x, y, w, h) in faces:
#     img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

# cv2.namedWindow('faces Detected!')
# cv2.imshow('faces Detected!',img)
# cv2.imwrite('faces.jpg',img)
# cv2.waitKey(0)

