import pygame
import pieces
import boards
from math import *
import squares
from game import *
from pygame.locals import *

def main():
    # Initialise screen
    possible_moves = []
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Board')
    
    board = boards.game_board()
    reset_board(screen, board)
    draw_bg(screen)
    update_board(screen, board, possible_moves)
    is_piece_selected = False
    selected_square = None
    clicking = False
    dragging = False
    

    # Event loop
    while True:

        #draws position of all pieces and squares
        draw_bg(screen)
        update_board(screen, board, possible_moves)

        #gets the current position of cursor and converts it to square
        pos = cursor_to_square(pygame.mouse.get_pos())

        #if left mouse button is being clicked 
        if(pygame.mouse.get_pressed()[0]==True):
            clicking = True



            #if a piece is being selected for the first time
            if(is_piece_selected==False):
                
                

                #updates selected square and selected piece
                selected_square = board.squares[pos[0]][pos[1]]
                selected_piece = selected_square.piece
                is_piece_selected = True

                #changes selected square color to be yellow
                for square_row in board.squares:
                    for square in square_row:
                        square.color = None

                #gets legal moves
                possible_moves = selected_piece.moves()
                show_possible_moves(possible_moves, screen)

                selected_square.color = (246,246,105,255)
            elif(pos[0]==selected_square.col-1 and pos[1]==selected_square.row-1):
                dragging = True
        
        if(clicking):
            if(pygame.mouse.get_pressed()[0]==False):
                clicking = False

                if(pos[0] != selected_square.col-1 or pos[1] != selected_square.row-1):
                    if(board.squares[pos[0]][pos[1]].piece):
                        if(board.squares[pos[0]][pos[1]].piece.color == selected_piece.color):
                            dragging = True
                            selected_square.show=True
                            selected_square = board.squares[pos[0]][pos[1]]
                            for square_row in board.squares:
                                for square in square_row:
                                    square.color = None

                            selected_square.color = (246,246,105,255)
                            selected_piece = selected_square.piece

           

        
       
    
       #if the left mouse button is not being clicked 
        else:
            
            dragging = False

            #if there is a piece selected
            if(is_piece_selected):
                if(clicking):

                
                
                    selected_square.show = False

                
               
                selected_square.show = True

        #checks if piece is being dragged and updates
        if(pygame.mouse.get_pressed()[0]==True and dragging):
            drag_piece(selected_piece.name, selected_piece.color, screen, pygame.mouse.get_pos())
            selected_square.show = False
        
       

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()


        pygame.display.update()


main()