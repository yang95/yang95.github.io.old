import cv2
import socket_server
#import web_socket
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
cap = cv2.VideoCapture(0)
while(1): 
    ret, frame = cap.read() 
    #frame = cv2.resize(frame.copy(),(320,240),interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)#gaussian
    
    #edge = cv2.Canny(gray.copy(), 1000, 2000, apertureSize=5)#bianjie
    ret, edge = cv2.threshold(gray,int(255*conf.threshold/100),255,cv2.THRESH_BINARY)

    edge = cv2.medianBlur(edge.copy(),15)
    _,contours, hierarchy = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #position
    for i in contours:
        x, y, w, h = cv2.boundingRect(i)
        #str_ = socket_server.to_position(x, y)
        poi = position.position(x, y) 
        if(poi != None):
            poi = position.view_position(a0,b0,x_m,y_m,poi[0], poi[1]) 
            socket_server.queue.put("%d,%d;"%(poi[0],poi[1]))
            #web_socket.queue.put(poi)
            print poi

    cv2.imshow("capture1", con_rect(edge))
    cv2.imshow("frame", con_rect(frame)) 
    # show a frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print frame
cap.release()
cv2.destroyAllWindows() 
