import pygame

class piece:
    def __init__(self, name, color, row, col):
        self.name = name
        self.color = color
        self.row = row
        self.col = col

    def display(self, screen):
        img = pygame.image.load(f"images\{self.color}\{self.name}.png")
        screen.blit(img, ((self.col*100)-90, 810-(self.row*100)))


class pawn(piece):
    def __init__(self, color, row, col):
        self.name = "pawn"
        self.color = color
        self.col = col
        self.row = row
    def moves(self):
        return [(self.col,self.row+1), (self.col, self.row+2)]

class rook(piece):
    def __init__(self, color, row, col):
        self.name= "rook"
        self.color = color
        self.col = col
        self.row = row

class knight(piece):
    def __init__(self, color, row, col):
        self.name= "knight"
        self.color = color
        self.col = col
        self.row = row
    def moves(self):
        return[(self.col-1, self.row+2),(self.col+1, self.row+2)]

class bishop(piece):
    def __init__(self, color, row, col):
        self.name= "bishop"
        self.color = color
        self.col = col
        self.row = row

class queen(piece):
    def __init__(self, color, row, col):
        self.name= "queen"
        self.color = color
        self.col = col
        self.row = row

class king(piece):
    def __init__(self, color, row, col):
        self.name= "king"
        self.color = color
        self.col = col
        self.row = row



