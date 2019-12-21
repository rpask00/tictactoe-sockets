import pygame
import os


class Grid():
    def __init__(self, imageX, imageO):
        self.grid_lines = [
            [(0, 200), (600, 200)],
            [(0, 400), (600, 400)],
            [(200, 0), (200, 600)],
            [(400, 0), (400, 600)]
        ]
        self.grid = [['', '', ''] for x in range(3)]
        self.imageX = imageX
        self.imageO = imageO
        self.winner = False

    def set_cell_value(self, x, y, value):
        if self.get_cell_value(x, y) != '':
            return False

        self.grid[y][x] = value
        return True

    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def print_grid(self):
        for g in self.grid:
            print(g)

    def check_for_winner(self):
        g = self.grid
        diagonal1 = [g[i][i] for i in range(3)]
        if diagonal1.count('X') == 3 or diagonal1.count('O') == 3:
            return [(100, 100), (500, 500)]
        diagonal2 = [g[2-i][2-i] for i in range(3)]
        if diagonal2.count('X') == 3 or diagonal2.count('O') == 3:
            return [(500, 100), (100, 500)]
        horizontal1 = g[0]
        if horizontal1.count('X') == 3 or horizontal1.count('O') == 3:
            return [(100, 100), (500, 100)]
        horizontal2 = g[1]
        if horizontal2.count('X') == 3 or horizontal2.count('O') == 3:
            return [(100, 300), (500, 300)]
        horizontal3 = g[2]
        if horizontal3.count('X') == 3 or horizontal3.count('O') == 3:
            return [(100, 500), (500, 500)]
        vertical1 = [row[0] for row in g]
        if vertical1.count('X') == 3 or vertical1.count('O') == 3:
            return [(100, 100), (100, 500)]
        vertical2 = [row[1] for row in g]
        if vertical2.count('X') == 3 or vertical2.count('O') == 3:
            return [(300, 100), (300, 500)]
        vertical3 = [row[2] for row in g]
        if vertical3.count('X') == 3 or vertical3.count('O') == 3:
            return [(500, 100), (500, 500)]

        return False

    def draw_lines(self, surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, (44, 6, 95), line[0], line[1], 5)

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == 'X':
                    surface.blit(self.imageX, (x*200, y*200))
                elif cell == 'O':
                    surface.blit(self.imageO, (x*200, y*200))

        if self.winner:
            pygame.draw.line(surface, (8, 0, 18), self.winner[0], self.winner[1], 25)
