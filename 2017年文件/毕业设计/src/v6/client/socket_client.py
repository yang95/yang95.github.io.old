import socket   
import time   
import mouse   
    
address = ('127.0.0.1', 8001)    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
while True:  
    try:
        print 'client connected server'
        s.connect(address)  
        break  
    except Exception, e:  
        time.sleep(0.1)  
        continue  
  
while True:    
    data = s.recv(512)  
    if len(data)>0:    
        poi_str = data.split(';',1)
        poi_str = poi_str[0]
        poi = poi_str.split(',')
        if(len(poi)>1 and poi[0]!='' and poi[1]!=''):
            print poi
            x = int(poi[0])
            y = int(poi[1])
            mouse.mouse_click(x,y)
        continue  
    else:  
        break   
    
s.close()  
