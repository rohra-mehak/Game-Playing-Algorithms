from concurrent.futures import thread
import os
from shutil import move 
import sys
import time
import random 

BLACK = "B"
WHITE = "W"
UP =  -8
DOWN = 8 
LEFT = -1 
RIGHT = 1
DIAGONAL_UPPER_LEFT = -9
DIAGONAL_UPPER_RIGHT = -7
DIAGONAL_LOWER_LEFT = 7
DIAGONAL_LOWER_RIGHT  = 9

directions = [UP, DOWN, LEFT, RIGHT, DIAGONAL_UPPER_LEFT, DIAGONAL_UPPER_RIGHT, DIAGONAL_LOWER_LEFT, DIAGONAL_LOWER_RIGHT]

def move_is_on_Board(move_index):
    """move made by the player must be a valid integer between 0 to 63 , as the reprsent the indices of the values on the board"""
    if move_index < 0 or move_index > 63:
       return False
    return True

def all_possible_moves(player, board):
    pass

def find_opponent_disc(move, board, player,dir):
    """find the place where the player's disc is in line with another of the player's disc and there are opponent's discs in between"""
    next_step = move + dir
    if move_is_on_Board(next_step):  
        if board[next_step]  == player:
           return None
        opponent=  (WHITE if player == BLACK else BLACK)

        while move_is_on_Board(next_step) and board[next_step] == opponent :
              next_step = next_step + dir
        if  move_is_on_Board(next_step) and board[next_step] != 0:
            return next_step
    return None

def make_board_copy(board):
    """produce a copy of the current board so check for valid moves .This ensures that no unnecessary changes are made oin the original board"""
    board_copy = [0 for j in range(len(board))]
    for i in range (len(board)):
        board_copy[i] = board[i] 
    return board_copy

def move_is_valid(player, move, board_copy, directions):
    found = None
    """check if the move can actually be made. 
    a move made by the payer is valid if it is on the board AND in line with one of the player's disc in any one of the directions, 
    AND there are opponent's disc between the player's discs. """
    if move_is_on_Board(move) and board_copy[move] == 0:
        possible_ways = []
        for dir in directions:
            found = (find_opponent_disc(move, board_copy, player, dir))
            if found is not None:
               possible_ways.append(dir)
               return True , possible_ways , found
    else :
        return False, [], found
    return False, [], found

            

def turn_opponents_disc(move, board, player, dir, step):
    """method to flip the opponent's disc into the player's disc once a valid move is made"""
    move = move + dir
    board_copy = make_board_copy(board)
    while step != move:
          board[move] = player 
          move = move + dir

def make_a_move(move, board, player):
    board[move] = player


def moves_are_left(board):
    for i in range(len(board)):
        if board[i] == 0:
         return True
    else :
        return False

def decide_winner(BLACK,board):
    black_ponts = 0 
    white_points = 0

    for i in range(len(board)):
        if board[i] == BLACK:
           black_ponts = black_ponts + 2
        else:
           white_points = white_points + 2
    if black_ponts > white_points:
        return F"BLACK WINS WITH {black_ponts} POINTS"
    elif white_points > black_ponts:
        return f"WHITE WINS WITH {white_points} POINTS"
    else :
        return "THE GAME WAS A DRAW"
        

def game_play(board):
    player = BLACK
    while moves_are_left(board):
          player_move = random.randint(0, len(board) -1)
          print(player, " " ,player_move)
          board_copy = make_board_copy(board)
          move_valid, valid_directions , step = move_is_valid(player, player_move,board_copy, directions)
          
          print(valid_directions)
          if move_valid and len(valid_directions) != 0:
             make_a_move(player_move, board, player)
             dir_ind = random.randrange(len(valid_directions))
             turn_opponents_disc(player_move, board, player, valid_directions[dir_ind] , step)
             opponet = WHITE if player == BLACK else BLACK
             player = opponet                
    print("GAME OVER")




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
    board = [
 0 , 0 , 0 ,   0 ,      0 ,      0 ,     0 ,    0 ,
 0,  0 , 0,    0 ,      0 ,      0 ,     0,     0 ,
 0,  0 , 0,    0 ,      0 ,      0 ,     0,     0 ,
 0,  0 , 0,    BLACK , WHITE ,   0 ,     0,     0 ,
 0,  0 , 0,    WHITE , BLACK ,   0 ,     0,     0 ,
 0,  0 , 0,    0 ,      0 ,      0 ,     0,     0 ,
 0,  0 , 0,    0 ,      0 ,      0 ,     0,     0 ,
 0,  0 , 0,    0 ,      0 ,      0 ,     0,     0 

]
    print(len(board))
    get_string_representation_of_board(board)
    game_play(board)
    get_string_representation_of_board(board)
    winner = decide_winner(BLACK,board)
    print(winner)