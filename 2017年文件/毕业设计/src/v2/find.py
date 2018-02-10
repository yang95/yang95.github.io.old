import cv2    
import numpy as np   
  
    
img = cv2.imread('img/0.jpg')    
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (21, 21), 0) 
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) 
    
_, contours, _ = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in contours:
    x, y, w, h = cv2.boundingRect(i)
    print x,y
cv2.drawContours(img,contours,-1,(0,0,255),3)    
    
cv2.imshow("img", img)    
cv2.waitKey(0)    
