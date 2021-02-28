import socket
from comm import formMSG, formMSG2, clearMsg

HOST = '192.168.10.254'  # Standard loopback interface address (localhost)
PORT = 7000        # Port to listen on (non-privileged ports are > 1023)

#pointApanha
#maxrange X 700
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(formMSG2("c_barra","ola",3))
    #s.sendall(formMSG2("readyg4","1",1))
    #s.sendall(formMSG2("apanhoug4","1",1))
    #s.sendall(formMSG2("XPOINTAPANHA", "{E6POS: X " + str(600.00) + ", Y " + str(0.0) + ", Z " + str(0.0) + ", A 0.47, B 0.52, C 37.34, S 6 , T 50}", 43981))
    #s.sendall(formMSG("ready", 3))
    #pointApanha
    s.sendall(formMSG2("MEEC2021_STATUS", "FALSE", 43981))

    data = s.recv(1024)
    clearMsg(data)