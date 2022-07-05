from concurrent.futures import thread
import os 
import sys
import time

BLACK = "B"
WHITE = "W"

board = [
 0 , 0 , 0 ,0 ,      0 ,      0 ,     0 ,    0 ,
 0,  0 , 0, 0 ,      0 ,      0 ,     0,     0 ,
 0,  0 , 0, 0 ,      0 ,      0 ,     0,     0 ,
 0,  0 , 0, BLACK , WHITE ,   0 ,     0,     0 ,
 0,  0 , 0, WHITE , BLACK ,   0 ,     0,     0 ,
 0,  0 , 0, 0 ,      0 ,      0 ,     0,     0 ,
 0,  0 , 0, 0 ,      0 ,      0 ,     0,     0 ,
 0,  0 , 0, 0 ,      0 ,      0 ,     0,     0 

]

def get_string_representation_of_board(board):
    board_rep = ""
    board_row = ""
    for i in range(len(board)) :
        board_row = board_row + f"| {board[i]} "
        if (i%8  == 7) :
            board_row = board_row + "\n" + "."*32 + "\n"
    board_rep = board_row  
    print(board_rep)


if __name__ == "__main__":
    print(len(board))
    get_string_representation_of_board(board)