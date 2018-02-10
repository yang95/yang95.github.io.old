import cv2
import numpy as np





frame = cv2.imread("img/3.png")
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

result = cv2.medianBlur(gray,5)

ret, edge = cv2.threshold(gray,250,255,cv2.THRESH_BINARY)
#edge = cv2.Canny(gray.copy(), 1000, 3000, apertureSize=5)#bianjie
_,contours, hierarchy = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #position
for i in contours:
    x, y, w, h = cv2.boundingRect(i)
    
cv2.imshow("gray", gray)  
cv2.imshow("result", result)  
cv2.imshow("edge", edge)  

cv2.waitKey(0)  
cv2.destroyAllWindows()   
