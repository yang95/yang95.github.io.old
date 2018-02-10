import cv2  
import numpy as np   
gray = cv2.imread("/Users/wzq/Desktop/testcase/h201703032044/73_38256928415637.jpg", cv2.IMREAD_GRAYSCALE)
 
bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 25)
