#--IMPORT
import socket
import time

#--VARIABILI
#server = "172.16.20.143"#Server Martino
#server = "172.16.3.219"#Server Sartori
#server = "172.16.3.230"#Server Pizzoli
#server = "172.16.3.231"#Server bragastini
server = "192.168.43.252"#Server mio
port = 2000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))



#--FUNZIONI
def online_users():
    pacchetto = bytearray()
    pacchetto.append(42)
    pacchetto.append(0)
    s.send(pacchetto)
    return pacchetto

def registerclient(user, password):
    newLogin = dataToBytes([user, password])
    pacchetto = bytearray()
    pacchetto.append(10)
    leng = len(newLogin).to_bytes(2, byteorder="big")
    pacchetto += leng
    pacchetto += newLogin
    s.send(pacchetto)
    return pacchetto

def login(user, password):
    Login = dataToBytes([user, password])
    pacchetto = bytearray()
    pacchetto.append(11)
    leng = len(Login).to_bytes(2, byteorder="big")
    pacchetto += leng
    pacchetto += Login

    s.send(pacchetto)
    return pacchetto

def dataToBytes(data):
    bytes = bytearray()
    for d in data:
        bytes += (bytearray(d.encode()))
        if data.index(d) != len(data) - 1:
            bytes.append(0)
    return bytes

def logout():
    pacchetto = bytearray()
    pacchetto.append(12)
    pacchetto.append(0)
    s.send(pacchetto)
    return pacchetto

def mex_recv():
    print(s)
    r = s.recv(1024)
    print("ciao")
    print(r)
    return r
#--MAIN
if __name__ == "__main__":


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    user, password = "ridosta", "sono_bellixxximo"
    #s.send(registerclient(user, password))
    s.send(login(user, password))
    r = mex_recv()
    print(r)
    #time.sleep(5)
    #s.send(logout())
    #r = s.recv(1024)
    #print(r)
    # nbyte=s.send(b'hello world!')
    # print("send", nbyte)
    # data = s.recv(1024)
    #
    # print('Received', str(data), len(data))
    while 1:
        pass

