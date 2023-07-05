#63011212055 ศิลาดล จันทร์นาหว้า
from socket import *

HOST = "127.0.0.1"
PORT = 9090
BUFSIZE = 4096
ADDRESS = (HOST, PORT)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(ADDRESS)
while True:
    print("##### Select Menu: #####\n")
    print("1:Login")
    print("2:Register")
    print("3:Exit")
    menu = input("\nEnter Menu:")
    menuT=str.encode(menu)
    sock.send(menuT)
    if menu == "1":
        user = input("UserName: ")
        pwd = input("Password: ")
        userName = str.encode(user)
        sock.send(userName)
        passwd = str.encode(pwd)
        sock.send(passwd)
        recvMessage = bytes.decode(sock.recv(BUFSIZE))
        print(recvMessage)
        print("\n")
        if recvMessage =="[SERVER] ~ Login  successfully ~":
            print("##### Select Menu: #####")
            print("1:Chat Group:")
            print("2:Client :(face-to-face)")
            print("3:Exit")
            print("\n")
            menu2 = input("Enter Menu:")
            menuT2=str.encode(menu2)
            sock.send(menuT2)
        if menu2 =='1':
            name = input("Enter your name:")
            userName = str.encode(name)
            sock.send(userName)
            while True:
                recvMessage = bytes.decode(sock.recv(BUFSIZE))
                if not recvMessage:
                    print("Disconnect from server !!!")
                    break
                print(recvMessage)
                sendMessage = input("> ")
                if sendMessage == 'Exit' or sendMessage == "exit" :
                    print("Disconnect from server!")
                    break
                sock.send(str.encode(sendMessage))
        else:
            break
    elif menu == "2":
        print("##### Register Menu: #####")
        user = input("UserName: ")
        pwd = input("Password: ")
        userName = str.encode(user)
        sock.send(userName)
        passwd = str.encode(pwd)
        sock.send(passwd)
        recvMessage = bytes.decode(sock.recv(BUFSIZE))
        print(recvMessage)
    elif menu =="3":
        print("Disconnect from server!")
        break 
sock.close
    
