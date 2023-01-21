import pieces
import pygame
import boards
import squares
from math import *


def show_possible_moves(possible_moves, screen):
    for move in possible_moves:
        pygame.draw.circle(screen, (175, 175, 175, 50), ((move[0]*100)-50, 820-(move[1]*100)+30), 20)


def drag_piece(piece, color,  screen, pos):
    img = pygame.image.load(f"images\{color}\{piece}.png")
    screen.blit(img, (pos[0]-40, pos[1]-40))

def cursor_to_square(pos):
    pos = ((floor(pos[0]/100))+1, 8-floor(pos[1]/100))       
    pos = (pos[0]-1, pos[1]-1)
    return pos

def update_board(screen, board, possible_moves):
    for row in board.squares:
        for square in row:
            if square.color and square.piece:
                boards.game_board.color_square(8-square.row, square.col-1, square.color, screen)
            if square.piece and square.show==True:
                square.piece.display(screen)
    show_possible_moves(possible_moves, screen)
           
def draw_bg(screen):
     for col in range(0,8):
        for row in range(0,8):
            
            if((col+row)%2==0):
                color=(234,235,200)
            else:
                color=(119,154,88)

            pygame.draw.rect(screen, color, (col*100, row*100,100,100))

def reset_board(screen, board): 
    for col in range(1, 9):
        tmp = []
        for row in range(1, 9):
            if row==1 or row==2:
                color="light"
            if row==7 or row==8:
                color="dark"


            if(row==2 or row==7):
                tmp.append(squares.square(row, col, pieces.pawn(color, row, col)))

            elif(row==1 or row==8):
                if(col == 1 or col == 8):
                    tmp.append(squares.square(row, col, pieces.rook(color, row, col)))
                
                if(col == 2 or col == 7):
                    tmp.append(squares.square(row, col, pieces.knight(color, row, col)))

                if(col == 3 or col == 6):
                    tmp.append(squares.square(row, col, pieces.bishop(color, row, col)))

                if(col == 4):
                    tmp.append(squares.square(row, col, pieces.queen(color, row, col)))    

                if(col == 5):
                    tmp.append(squares.square(row, col, pieces.king(color, row, col)))
            
            else:
                tmp.append(squares.square(row, col))

        board.squares.append(tmp)
    
            

          
    
   



    



