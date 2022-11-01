import cv2
import os


car_cascade = cv2.CascadeClassifier('C:/Users/MAYUR/Desktop/two_wheeler.xml')
cap = cv2.VideoCapture(0)




while True:
  
    success, img = cap.read()
    
    # convert to gray scale of each img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    
    # To draw a rectangle in each cars
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, 'bike', (x + 6, y - 6), font, 0.5, (0, 0, 255), 1)
        
        
        # Display img in a window
    cv2.imshow('Car Detection', img)
    
    
    # Wait for Enter key to stop
    if cv2.waitKey(33) == 13:
        break

cap.release()
cv2.destroyAllWindows()