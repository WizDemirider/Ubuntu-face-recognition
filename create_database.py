'''
create a database by capturing frames from webcam
'''

import cv2
import os
import time

count=100

person_name = input("Enter your name")
database_dir = '/home/ankit/Documents/database'
path = os.path.join(database_dir,person_name)
if not os.path.isdir(path):
    os.mkdir(path)

face_cascade = cv2.CascadeClassifier("/home/ankit/Documents/face_detection_models/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while (count < 200):
    ret_val, frame = cap.read()
    if ret_val == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,5)
        if list(faces):
            face = max(faces, key = lambda x:x[2]*x[3])
            roi = gray[face[1]:face[1]+face[3],face[0]:face[0]+face[2]]
            roi = cv2.resize(roi,(100,100))
            cv2.imwrite(path+'/'+str(count)+'.jpg',roi)
    count=count+1
    time.sleep(2)
    cv2.imshow("image",gray)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cv2.waitKey(100)
            
cap.release()

            
