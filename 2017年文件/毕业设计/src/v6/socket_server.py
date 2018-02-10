from socket import * 
import thread 
from Queue import Queue  

queue = Queue()
def Init(sock):  
        while True:
            print('waiting for connection')
            tcpClientSock, addr=sock.accept()
            print('connect from ', addr)
            while True:
                while queue.empty() == False: 
                        val = queue.get(0)   
                        tcpClientSock.send(val.encode('utf8'))
        tcpClientSock.close()
        sock.close()



HOST=''
PORT=8001
BUFSIZ=1024
ADDR=(HOST, PORT)
sock=socket(AF_INET, SOCK_STREAM)

sock.bind(ADDR)

sock.listen(5) 
try:
        thread.start_new_thread( Init , (sock,)) 
except:
        print "Error: unable to start thread" 
