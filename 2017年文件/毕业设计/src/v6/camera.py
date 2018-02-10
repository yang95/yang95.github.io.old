import cv2
import numpy as np
import thread
from Queue  import Queue
from conf_data import conf_data

f_queue = Queue()


def Init(cap): 
    while(1): 
        ret, frame = cap.read()
        conf = conf_data()
        conf.load()
        conf.to_int()
        cv2.line(frame,(conf.x0,conf.y0),(conf.x1,conf.y1),(255,0,0),5)
        cv2.line(frame,(conf.x1,conf.y1),(conf.x2,conf.y2),(255,0,0),5)
        cv2.line(frame,(conf.x2,conf.y2),(conf.x3,conf.y3),(255,0,0),5)
        cv2.line(frame,(conf.x3,conf.y3),(conf.x0,conf.y0),(255,0,0),5)

        cv2.imshow("capture2", frame) 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
    cap.release()
    cv2.destroyAllWindows() 


cap = cv2.VideoCapture(0)

 
 
try:
        thread.start_new_thread( Init , (cap,)) 
except:
        print "Error: unable to start thread" 
