import pygame
from grid import Grid
import threading
from threading import Timer
from network import Network
from _thread import *
import os
import pickle
import socket


running = True
os.environ['SDL_VIDEO_WINDOW_POS'] = '-860, 200'
surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tictactoe')
grid = Grid()
n = Network()
turn = n.id == 'O'


def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()


def receive_data():
    global running, turn
    while running:
        grid.grid, turn = pickle.loads(n.client.recv(1000))
        print('received ', grid.grid, ' ', turn)
        grid.winner = grid.check_for_winner()

create_thread(receive_data)


while running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not grid.winner:
                pos = pygame.mouse.get_pos()
                cords = (pos[0] // 200, pos[1] // 200)
                if pygame.mouse.get_pressed()[0]:
                    if turn:
                        n.client.send(pickle.dumps((cords, n.id)))

    except socket.error as err:
        print(str(err))

    surface.fill((255, 255, 255))
    grid.draw_lines(surface)
    pygame.display.flip()
