import socket
import json
import time
import numpy as np
import pandas as pd

msgFromClient       = "200"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 20000
UDPClientSocket     = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

def out():
    dat =[]
    for i in range(1):
        for i in range(10):
            
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            dec = json.loads(msgFromServer[0].decode())

            a = dec.get("a")
            b = dec.get("b")
            c = dec.get("c")
            d = dec.get("d")

            x = a,b,c,d
            dat.append(x)
            
    dat = np.array(dat)
    df = pd.DataFrame(dat)
    df.columns = ['data1','data2','data3','data4']
    print(df)
    

while True :
    out()
   