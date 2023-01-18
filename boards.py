import squares
import pygame

class game_board:
    def __init__(self):
        self.squares = []
    
    def color_square(row, col, color, screen):
        pygame.draw.rect(screen, color, (col*100, row*100,100,100))


    