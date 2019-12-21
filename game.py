import pygame
import os
from grid import Grid
from threading import Timer

imageX = pygame.image.load(os.path.join('assets', 'x.png'))
imageO = pygame.image.load(os.path.join('assets', 'o.png'))

os.environ['SDL_VIDEO_WINDOW_POS'] = '900, 250'
surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tictactoe')
running = True
player = 'X'

grid = Grid(imageX, imageO)
grid.print_grid()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] and not grid.winner:

                pos = pygame.mouse.get_pos()
                cords = (pos[0] // 200, pos[1] // 200)

                if(grid.set_cell_value(cords[0], cords[1], player)):
                    player = 'O' if player == 'X' else 'X'
                    grid.print_grid()
                    grid.winner = grid.check_for_winner()

        surface.fill((63, 151, 5))
        grid.draw_lines(surface)
        pygame.display.flip()
