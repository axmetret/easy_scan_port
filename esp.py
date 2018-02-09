import socket
import sys
x=22
host=input("Enter the host: ")
for port in x:
    try:
        s=socket.socket()
        s.settimeout(0.5)
    except:
        pass
    else:
        s.close
        print (host + ':' + str(port) + '[Connect]')
