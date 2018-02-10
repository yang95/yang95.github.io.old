import cv2
import numpy as np

threshod= 100

def pic_sub(dest,s1,s2):
    for x in range(dest.shape[0]):
        for y in range(dest.shape[1]):
            if(s2[x,y] > s1[x,y]):
                dest[x,y] = s2[x,y] - s1[x,y]
            else:
                dest[x,y] = s1[x,y] - s2[x,y]

            if(dest[x,y] < threshod):
                dest[x,y] = 0
            else:
                dest[x,y] = 255




img0 = cv2.imread('img/1.png')   
gray0 = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)  
gray0 = cv2.GaussianBlur(gray0, (21, 21), 0)  



cap = cv2.VideoCapture(0)
while(1):
    # get a frame
    ret, frame = cap.read()
    frame = frame[0:250,0:250,:]
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    edge = cv2.Canny(gray.copy(), 1000, 2000, apertureSize=5)
    _,contours, hierarchy = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    for i in contours:
        x, y, w, h = cv2.boundingRect(i)
        print x,y

    cv2.imshow("capture1", edge)
    cv2.imshow("capture2", frame)
    cv2.imshow("capture3", gray)
    # show a frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print frame
cap.release()
cv2.destroyAllWindows() 
