import cv2
import numpy as np
#only red light can be catch

def Strengthen(img):
    for i in img :
        for j in img[i]:
            print img[i][j]


cap = cv2.VideoCapture(0)
while(1):
    # get a frame
    ret, frame = cap.read() 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  
    #gray = cv2.GaussianBlur(gray, (21, 21), 1)#gaussian
    
    edge = cv2.Canny(gray.copy(), 1000, 3000, apertureSize=5)#bianjie
    _,contours, hierarchy = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #position
    for i in contours:
        x, y, w, h = cv2.boundingRect(i)
        #print x,y

    cv2.imshow("edge", edge)
    cv2.imshow("gray", gray) 
    cv2.imshow("frame", frame) 
    # show a frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
    if cv2.waitKey(1) & 0xFF == ord('s'):
        Strengthen(gray) 
cap.release()
cv2.destroyAllWindows() 
