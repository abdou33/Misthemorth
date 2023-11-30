import os
import cv2
import time
import uuid

labels=['Hello','Yes','No','Thanks','IloveYou','Please']

number_of_images=20

for label in labels:
    cap=cv2.VideoCapture(0)
    for imgnum in range(number_of_images):
        ret,frame=cap.read()
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()