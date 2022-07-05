from concurrent.futures import thread
import os 
import sys
import time 

def return_string_representation_of_board(board):
    """The method prints out the list of ints on the board as a 9 x 9 string representation of the sudoku board """
    board_rep = ""
    board_row = ""
    for i in range(81) :
        board_row = board_row + f"| {board[i]} "
        if (i%9  == 8) :
            board_row = board_row + "\n" + "."*36 + "\n"
    board_rep = board_row
    print(board_rep)
   

def empty_cell(board):
    """method to  return the index of the empty cell ,if it exists."""
    for i in range(len(board)):
        if board[i] == 0:
           return i
    return None

def is_insertion_valid(board, cell_index, value):
    """method to check if the value being inserted in the cell is valid at that position.
    This is being done by evalutaing the cells coressponding row, col and box """
    col = cell_index % 9
    row = (cell_index - col) // 9

    for i in range(0,9):
        if board[i + (9*row)] == value:
           return False
    
    for i in range(0,9):
        if board[(i*9) +col ] == value:
            return False
    
    start_row = (row // 3) * 3
    start_col = (col // 3 )* 3

    for k in range(start_row, start_row +3):
        for l in range(start_col, start_col+3):
             if board[(9*k) + l] == value:
                 return False
    return True

def solve_sudoku(board):
    """The resursive backtracker which solves the board by looking for an empty cell, checking for a valid insertion and backtracking at an incorrect guess."""
    cell_index = empty_cell(board)

    if cell_index is None:
        return True
    else :
        index = cell_index

    for value in range(1, 10):
        if is_insertion_valid(board, index, value):
            board[index] = value
            if solve_sudoku(board):
                return True
            board[index] = 0

    return False

if __name__ == "__main__":
    board = [
    7, 8, 0, 4, 0, 0, 1, 2, 0,
    6, 0, 0, 0, 7, 5, 0, 0, 9,
    0, 0, 0, 6, 0, 1, 0, 7, 8,
    0, 0, 7, 0, 4, 0, 2, 6, 0,
    0, 0, 1, 0, 5, 0, 9, 3, 0,
    9, 0, 4, 0, 6, 0, 0, 0, 5,
    0, 7, 0, 3, 0, 0, 0, 1, 2,
    1, 2, 0, 0, 0, 7, 4, 0, 0,
    0, 4, 9, 2, 0, 6, 0, 0, 7
    ]
    return_string_representation_of_board(board)
    start = time.time()
    solve_sudoku(board)
    stop = time.time()
    return_string_representation_of_board(board)
    print(f" \n Method execution Time-> {stop - start} ms")

    
    