import cv2    
import numpy as np   
  
img0 = cv2.imread('img/1.png')    
gray0 = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)  
gray0 = cv2.GaussianBlur(gray0, (21, 21), 0)    

       
img = cv2.imread('img/3.png')    
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
gray = cv2.GaussianBlur(gray, (21, 21), 0)    
    
cv2.imshow("img0", gray0) 
cv2.imshow("img", gray)   
cv2.waitKey(0)    
