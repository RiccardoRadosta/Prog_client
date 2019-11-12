#--IMPORT
import socket
import time
#--VARIABILI
server = "172.16.20.143"#da aggiungere quando qualcuno creera un server
port = 2000

#--FUNZIONI
def register(user, password):
    newLogin = dataToBytes([user, password])
    pacchetto = bytearray()
    pacchetto.append(10)
    leng = len(newLogin).to_bytes(2, byteorder="big")
    pacchetto += leng
    pacchetto += newLogin
    return pacchetto

def login(user, password):
    Login = dataToBytes([user, password])
    pacchetto = bytearray()
    pacchetto.append(11)
    leng = len(Login).to_bytes(2, byteorder="big")
    pacchetto += leng
    pacchetto += Login
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
    return pacchetto
#--MAIN
if __name__ == "__main__":


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    user, password = "ridosta", "sono_bellixxximo"
    #s.send(register(user, password))
    s.send(login(user, password))
    r = s.recv(1024)
    print(r)
    time.sleep(10)
    s.send(logout())
    r = s.recv(1024)
    print(r)
    # nbyte=s.send(b'hello world!')
    # print("send", nbyte)
    # data = s.recv(1024)
    #
    # print('Received', str(data), len(data))
    while 1:
        pass

