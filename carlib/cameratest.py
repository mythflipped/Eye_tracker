import cv2
import numpy as np

cap_Left = cv2.VideoCapture(1)
cap_Right = cv2.VideoCapture(0)

while True:
    ret, frame_Left = cap_Left.read()
    ret, frame_Right = cap_Right.read()
    if not ret:
        break
    cv2.imshow('left', frame_Left)
    cv2.imshow('right', frame_Right)
    k = cv2.waitKey(1)
    if k == ord('q'):
        cv2.imwrite('left.jpg', frame_Left)
        cv2.imwrite('right.jpg', frame_Right)

cap_Left.release()
cap_Right.release()
cv2.destroyAllWindows()



