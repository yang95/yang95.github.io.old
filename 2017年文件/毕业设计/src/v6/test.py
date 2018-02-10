import cv2
import numpy as np

img_pre = None
def Init(cap):
    global img_pre
    while(1):
        ret, frame = cap.read()
        if (img_pre == None):
            img_pre = frame.copy()

        tmp=frame-img_pre


        gray = cv2.cvtColor(tmp,cv2.COLOR_BGR2GRAY)
        #gray = cv2.GaussianBlur(gray, (21, 21), 0)#gaussian
        #gray = cv2.medianBlur(gray,6)
        gray = cv2.blur(gray,(100,100))
        ret,edge = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
        #edge = cv2.Canny(tmp.copy(), 1000, 2000, apertureSize=5)#bianjie
        _,contours, hierarchy = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #position
        for i in contours:
            x, y, w, h = cv2.boundingRect(i)
            print x,y

        #cv2.imshow("img_pre", img_pre)
        cv2.imshow("frame", tmp)
        cv2.imshow("gray", gray)
        img_pre = frame.copy()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)
Init(cap)
