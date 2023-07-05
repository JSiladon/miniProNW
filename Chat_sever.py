#63011212055 ศิลาดล จันทร์นาหว้า
from socket import *
from DiChatDB1 import chatDB
from threading import Thread
import threading
from time import ctime

class clientHandler(Thread):
    def __init__(self,client,record,address):
        Thread.__init__(self)
        self._client = client
        self._record = record
        self._address = address
    def boardcastMessage(self,activeClient,message):
        for socket in CONNECTIONS_LIST:
            if socket != server and socket != activeClient:
                try:
                    msg = str.encode(message)
                    socket.send(msg)
                except:
                    print("Client (%s) is ofline"%self._address)
                    broadcastMessage(socket,("Client(%s) is proably offline" %self._address))
                    socket.close
                    CONNECTIONS_LIST.remove(socket)
    def run(self):
        while True:
            self._menu = bytes.decode(self._client.recv(BUFSIZE))
            self._menu = self._menu.strip()
            if self._menu == "1":
                recv_nameloing = bytes.decode(self._client.recv(BUFSIZE))
                recv_pwd = bytes.decode(self._client.recv(BUFSIZE))
                myUser = []
                f = open("user.txt", "r")
                for nameloing in f:
                    myUser.append(nameloing.strip())
                myPasswd = []
                f = open("passwd.txt", "r")
                for pwd in f:
                    myPasswd.append(pwd.strip())
                if recv_nameloing in myUser and recv_pwd  in myPasswd:
                    self._client.send(str.encode("[SERVER] ~ Login  successfully ~"))
                    self._menu = bytes.decode(self._client.recv(BUFSIZE))
                    self._menu = self._menu.strip()
                    if self._menu == "1":
                        self._name = bytes.decode(self._client.recv(BUFSIZE))
                        self._client.send(str.encode("Welcome to the chat room !! :["+self._name+"]"))
                        while True:
                            message = bytes.decode(self._client.recv(BUFSIZE))
                            if not message:
                                print("Client disconnected")
                                self._client.close()
                                CONNECTIONS_LIST.remove(self._client)
                                break
                            else:
                                message = ctime()+" :["+self._name+ "] -->"+message
                                f = open("allmessage.txt", "a")
                                f.write(message+"\n")
                                f.close()
                                print(message)
                                threadLock.acquire()
                                self.boardcastMessage(self._client,message)
                                threadLock.release()
                                self._client.send(str.encode("[SERVER] ~ Sent message successfully ~"))
                    else:
                        pass        
                else:
                    self._client.send(str.encode("[SERVER] ~ Login  unsuccessfully ~\n"))
                    print("\n")
            elif self._menu == "2":
                name = bytes.decode(self._client.recv(BUFSIZE))
                f = open("user.txt", "a")
                f.write(name+"\n")                

                passwd = bytes.decode(self._client.recv(BUFSIZE))
                pa = open("passwd.txt", "a")
                pa.write(passwd+"\n")  
                self._client.send(str.encode("[SERVER] ~ Register  successfully ~\n"))
                print("\n")
HOST = "127.0.0.1"
PORT = 9090
BUFSIZE = 4096
ADDRESS = (HOST, PORT)
CONNECTIONS_LIST = []
threadLock = threading.Lock()
record = chatDB()  #name import class
server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDRESS)
MAX_CLIENT = 250
server.listen(MAX_CLIENT)
CONNECTIONS_LIST.append(server)
print("Chat server has started on port: ", PORT)
while True:
    print("Waiting for a connect...")
    client,address = server.accept()
    print("... connection", address)
    threadLock.acquire()
    CONNECTIONS_LIST.append(client)
    threadLock.release()
    handler = clientHandler(client,record,address)
    handler.start()





        
