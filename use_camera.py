import cv2
import time

capture = cv2.VideoCapture(0)
time.sleep(1)

while True:
    ret, frame = capture.read()
    # flipping the frame
    frame = cv2.flip(frame,1)
    cv2.imshow("video", frame)
    key = cv2.waitKey(50)

    if key  == ord('q'):  # press q to exit
        break
cv2.destroyAllWindows()
