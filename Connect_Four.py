import numpy as np
import math
import pygame
import sys

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Horizontal check
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Vertical check
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True 
    
    # Diagonal check
    # NE direction


    # NW direction

def draw_board(board):
    pass

board = create_board()
game_over = False
print_board(board)
turn = 0

while not game_over:
    # Player 1 Input
    if turn == 0:
        selection = int(input("Player 1 Make your Selection (0-6)"))

        if is_valid_location(board, selection):
            row = get_next_open_row(board, selection)
            drop_piece(board, row, selection, 1)

            if winning_move(board, 1):
                print("PLAYER 1 Wins")
                game_over = True
    
    # Player 2 Input
    else:
        selection = int(input("Player 2 Make your Selection (0-6)"))

        if is_valid_location(board, selection):
            row = get_next_open_row(board, selection)
            drop_piece(board, row, selection, 2)

            if winning_move(board, 2):
                print("PLAYER 2 Wins")
                game_over = True
            
    print_board(board)

    turn += 1
    turn = turn % 2 