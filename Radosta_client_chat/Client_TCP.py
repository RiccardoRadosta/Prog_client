#--IMPORT
import socket

#--VARIABILI
server = ""#da aggiungere quando qualcuno creera un server
port = 7

#--FUNZIONI
def register(user, password):
    newLogin = dataToBytes([user, password])

    pacchetto = bytearray()
    pacchetto.append(10)

    leng = len(newLogin).to_bytes(2, byteorder="big")
    pacchetto += leng

    pacchetto += newLogin

    return pacchetto



def dataToBytes(data):
    bytes = bytearray()
    for d in data:
        bytes += (bytearray(d.encode()))
        if data.index(d) != len(data) - 1:
            bytes.append(0)
    return bytes

def login():
    a = 43

#--MAIN
if __name__ == "__main__":


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    user, password = "tognella", "password"
    s.send(register(user, password))


    # nbyte=s.send(b'hello world!')
    # print("send", nbyte)
    # data = s.recv(1024)
    #
    # print('Received', str(data), len(data))
    s.close()
