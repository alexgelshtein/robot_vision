import socket
import time
from detection import detect

HOST = "169.254.54.150" 
PORT = 30000 

print ("Starting Program")
count = 0

while count < 5:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT)) 
    s.listen(5)
    c, addr = s.accept()
    try:
        msg = c.recv(1024)
        print ("Request = ", msg)
        
        detect()

        c.send(b"(123)")
        print("Sent 123")
        count += 1

    except socket.error as socketerror:
        print (socketerror)
 
c.close()
s.close()
print ("Program finish")