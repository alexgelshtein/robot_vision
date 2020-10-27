import socket
import time
from detection import detect

HOST = "169.254.54.150" 
PORT = 30000 

tmp = 0

while tmp < 5: 
    print ("Connecting to robot")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    c, addr = s.accept()
    print ("Connected by ", addr)
    print ("Loop № ", tmp + 1)
    try:
        msg = c.recv(1024)
        print ("Starting prog {}".format(tmp))
            
        time.sleep(5)
        print('Prog done')
        time.sleep(1)

        c.send(b"(123)")
        print("Stopping robot")
        tmp += 1

    except socket.error as socketerror:
        print (socketerror)

c.close()
s.close()
print ("Disconnected")