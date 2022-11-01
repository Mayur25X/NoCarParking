import cv2
import pickle
import cvzone
import numpy as np

cap=cv2.VideoCapture(0)

def chekParkingSpace(imgpro):
    
     x,y=50,100
     imgcrop=imgpro[y:y+100,x:x+50]
     cv2.imshow('sgo',imgcrop)
     count=cv2.countNonZero(imgcrop)
     cvzone.putTextRect(img,str(count), (x,y),scale=1.5,offset=0,thickness=2)
     if count==0:
          color=(0,255,0)
          thickness=5
          cv2.rectangle(img,(200,100),(100,300),color,thickness)
     else:
          color=(0,0,255)
          thickness=3
          cv2.rectangle(img,(200,100),(100,300),color,thickness)
     
     
while True:
    success, img = cap.read()
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBulr=cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold=cv2.adaptiveThreshold(imgBulr,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgMedian=cv2.medianBlur(imgThreshold,5)
    kernel=np.ones((3,3),np.uint8)
    imgDilate=cv2.dilate(imgMedian,kernel,iterations=1)
    
    chekParkingSpace(imgDilate)
  
    cv2.imshow('Car Detection', img) 
#     cv2.imshow('blur',imgBulr)
#     cv2.imshow('Threshold',imgMedian)
    cv2.waitKey(1)  
    