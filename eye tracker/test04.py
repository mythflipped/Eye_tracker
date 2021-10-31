import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


def detect_faces(img, cascade):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    coords = cascade.detectMultiScale(gray_frame, 1.3, 5)
    if len(coords) > 1:
        biggest = (0, 0, 0, 0)
        for i in coords:
            if i[3] > biggest[3]:
                biggest = i
        biggest = np.array([i], np.int32)
    elif len(coords) == 1:
        biggest = coords
    else:
        return None
    for (x, y, w, h) in biggest:
        frame = img[y:y + h, x:x + w]
    return frame


def detect_eyes(img, cascade):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = cascade.detectMultiScale(gray_frame, 1.3, 5)  # detect eyes
    width = np.size(img, 1)  # get face frame width
    height = np.size(img, 0)  # get face frame height
    left_eye = None
    right_eye = None
    for (x, y, w, h) in eyes:
        if y > height / 2:
            pass
        eyecenter = x + w / 2  # get the eye center
        if eyecenter < width * 0.5:
            left_eye = img[y:y + h, x:x + w]
        else:
            right_eye = img[y:y + h, x:x + w]
    return left_eye, right_eye

img = cv2.imread("qing2.jpg")
gray_picture = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # make picture gray
faces = face_cascade.detectMultiScale(gray_picture, 1.3, 5)



for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

#output1
cv2.imshow('my image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_face = gray_picture[y:y+h, x:x+w] # cut the gray face frame out
face = img[y:y+h, x:x+w] # cut the face frame out
eyes = eye_cascade.detectMultiScale(gray_face)

for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(face,(ex,ey),(ex+ew,ey+eh),(0,225,255),2)

#output2
cv2.imshow('my image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

