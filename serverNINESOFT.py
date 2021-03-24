import socket
import threading
import time

class Cserver(threading.Thread):
    def __init__(self, socket):
        super().__init__()
        self.s_socket = socket
        self.clients_Num = 0

    def run(self):
        global index
        global clients
        self.c_socket, addr = self.s_socket.accept()
        clients.append(self.c_socket)
        self.clients_Num = len(clients)
        print('All Workers: ', self.clients_Num, addr[0], addr[1], 'are connected')
        index = index + 1
        creat_thread(self.s_socket)
        t = threading.Thread(target=self.c_recv)
        t.daemon = True
        t.start()

    def c_recv(self):
        print(self.c_socket)
        while True:
            get_data= self.c_socket.recv(1024)
            get_data_str = str(get_data.decode('utf-8'))
            get_data_spl = get_data_str.split()
            print('Worker: ', get_data.decode('utf-8'))
            time.sleep(3)

            #print('Worker: ', get_data_spl[0], get_data.decode('utf-8'))
            """
            for i in range(self.clients_Num):
                get_data[i] = clients[i].c_socket.recv(1024)
            time.sleep(3)
            for i in range(self.clients_Num):
                print(get_data[i].decode('utf-8'))
            time.sleep(3)
            """

    #def c_send(self,put_data):
    #   self.c_socket.send(put_data.encode('utf-8'))


def creat_thread(s_socket):
    global index
    t.append(Cserver(s_socket))
    t[index].daemon = True
    t[index].start()


t=[]
index=0
clients = []
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

bufsize= 1024
host= input("Welcome to NINESOFT Server \n Enter the Server IP:")
port=9999
s_socket.bind((host, port))
s_socket.listen(5)
creat_thread(s_socket)

while True:
    pass
    #st_data = input('Message to send:' + '\n')
    #c_socket.send(st_data.encode('utf-8'))

s_socket.close()

"""
while True:
    try:
        for i in t:
            i.c_send(put_data)

    except Exception as e:
        pass

  
    for j in t:
        try:
            j.c_socket.close()
        except Exception as e:
            pass
"""








"""
def data_recv():
    while True:
        get_data = c_socket.recv(1024)
        print(get_data.decode('utf-8'))



s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

bufsize = 1024
host="127.0.0.1"
port=5001
s_socket.bind((host, port))
s_socket.listen(5)
c_socket, addr = s_socket.accept()
print(addr,"has been connected")

t = threading.Thread(target = data_recv)
t.daemon = True
t.start()


while True:
    st_data = input('Message to send:' + '\n')
    c_socket.send(st_data.encode('utf-8'))
    #time.sleep(3)



c_socket.close()
s_socket.close()
"""
