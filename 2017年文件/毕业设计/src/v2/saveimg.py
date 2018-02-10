import cv2
import numpy as np 
 

cap = cv2.VideoCapture(0)
while(1):
    # get a frame
    ret, frame = cap.read()
    frame = frame[0:400,0:400,:]
    gray = cv2.GaussianBlur(frame, (21, 21), 0) 
    cv2.imshow("capture", gray)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("img/1.png", gray)  
        break
cap.release()
cv2.destroyAllWindows() 
