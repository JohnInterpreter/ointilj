from socket import *
import threading
import extract3333 as ex3333
import time
import struct


"""
def data_recv():
    while True:
        get_data=s_socket.recv(1024)
        print(get_data.decode('utf-8'))
"""

#myName = input('Enter Your Nickname')

bufsize = 1024
host = input("Welcome to NINESOFT Client \n Enter the Server IP:")
port = 9999
dataToSend = b''


"""
t=threading.Thread(target=data_recv)
t.daemon=True
t.start()
"""

s_socket = socket(AF_INET, SOCK_STREAM)
s_socket.connect((host, port))

ExtCl = ex3333.Extract()

while True:
    """put_data = input("transmit:")
    if put_data == '1':
        break
    """
    #GPU 정보를 가져오는 함수를 호출하여, dataToSend에 담아서 보냅니다.과부하를 막기위해 3초의 여유를 둡니다.
    ExtCl.findGPU()
    dataToSend = ExtCl.dataToSend
    s_socket.send(dataToSend)
    time.sleep(3)

    #s_socket.close()

    #port += 1

    #get_cs=s_socket.recv(bufsize)
    #print(get_cs.decode('utf-8'))



