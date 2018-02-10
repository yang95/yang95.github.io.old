import cv2
import socket_server 
import numpy as np
import position
from conf_data import conf_data


conf = conf_data()
conf.load()
conf.to_int()

def con_rect(frame): 
    cv2.line(frame,(conf.x0,conf.y0),(conf.x1,conf.y1),(255,0,0),5)
    cv2.line(frame,(conf.x1,conf.y1),(conf.x2,conf.y2),(255,0,0),5)
    cv2.line(frame,(conf.x2,conf.y2),(conf.x3,conf.y3),(255,0,0),5)
    cv2.line(frame,(conf.x3,conf.y3),(conf.x0,conf.y0),(255,0,0),5)
    return frame

position.textture(conf.x0,conf.y0,conf.x1,conf.y1,conf.x2,conf.y2,conf.x3,conf.y3);
a0 = conf.a0
b0 = conf.b0
x_m = conf.a2-conf.a0
y_m = conf.b2-conf.b0
img_pre = None
def Init(cap):
    global img_pre
    while(1):
        ret, frame = cap.read() 
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#gray
        
        gray = cv2.equalizeHist(gray) 
        #gray = cv2.GaussianBlur(gray, (21, 21), 0)#gaussian
        #gray = cv2.medianBlur(gray,6)

        if (img_pre == None):
            img_pre = gray.copy()#previous image

        tmp=gray-img_pre #the difference
        
        img_pre = gray.copy()#update previous image

        
        ret,edge = cv2.threshold(tmp,200,255,cv2.THRESH_BINARY)#threshold

         
        
        
        #edge = cv2.blur(tmp,(5,5))#noise removal
        #edge = cv2.GaussianBlur(tmp,(105,105),20)   
        edge = cv2.medianBlur(tmp.copy(),115)
        #edge = cv2.Canny(tmp.copy(), 1000, 2000, apertureSize=5)#bianjie
        _,contours, hierarchy = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #position
        for i in contours:
            x, y, w, h = cv2.boundingRect(i)
            poi = position.position(x, y) 
            if(poi != None):
                break
                #poi = position.view_position(a0,b0,x_m,y_m,poi[0], poi[1]) 
                #socket_server.queue.put("%d,%d;"%(poi[0],poi[1]))
                #web_socket.queue.put(poi)
                #print poi

        cv2.imshow("img_pre", img_pre)
        cv2.imshow("frame", frame)
        cv2.imshow("tmp", edge)
        #cv2.imshow("edge", edge)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)
Init(cap)
