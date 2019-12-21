import socket
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '192.168.100.105'
port = 4444

try:
    s.bind((server, port))
except socket.error as err:
    print(str(err))

s.listen(2)
print('Waiting for connection...')


def maintain_client_thread(connection):
    while True:
        try:
            data = connection.recv(2048)
            reply = data.decode('utf-8')

            if not data:
                connection.send('End of connection ;(')
            else:
                print('Received: ' + reply)
                # doo smth...
            respond_val = ''
            connection.sendall(str.encode(respond_val))
        except:
            break

    print('Connection closed')
    connection.close()


while True:
    conn, addr = s.accept()
    print('Connected to: ', addr)

    start_new_thread(maintain_client_thread, conn)
