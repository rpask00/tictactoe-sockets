import socket
from _thread import *
from grid import Grid
import pickle
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '192.168.100.105'
port = 4444

try:
    s.bind((server, port))
except socket.error as err:
    print(str(err))

s.listen(2)
print('Waiting for connection...')
currentId = 'X'
turn = 0
grid = Grid()
my_clients = []


def maintain_client_thread(conn, addr):
    global currentId, turn
    local_id = currentId
    conn.send(str.encode(currentId))
    currentId = 'O'

    while True:
        try:
            cords, ID = pickle.loads(conn.recv(1000))
            if not cords:
                for i, c in enumerate(my_clients):
                    c.send(pickle.dumps((grid.grid, turn % 2 == i)))
            else:
                if grid.set_cell_value(cords, ID):
                    for i, c in enumerate(my_clients):
                        c.send(pickle.dumps((grid.grid, turn % 2 == i)))
                    turn += 1

        except socket.error as err:
            print(str(err))
            break

    print('Connection closed ', local_id)
    conn.close()


while True:
    conn, addr = s.accept()
    print('Connected to: ', addr)
    my_clients.append(conn)
    start_new_thread(maintain_client_thread, (conn, addr))
