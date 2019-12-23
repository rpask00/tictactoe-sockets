import socket
import pickle


class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '192.168.100.105'
        self.port = 4444
        self.addr = (self.host, self.port)
        self.id = self.connect()

    def connect(self):
        self.client.connect(self.addr)
        # self.client.send(str.encode('hello'))
        return self.client.recv(2048).decode()

    def exchange(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as err:
            return str(err)
