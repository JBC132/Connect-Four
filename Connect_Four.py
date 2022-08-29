import numpy as np
import math
import pygame
import sys

def create_board():
    board = np.zeros((6,7))
    return board

board = create_board()
game_over = False
turn = 0

while not game_over:
    # Player 1 Input
    if turn == 0:
        selection = int(input("Player 1 Make your Selection (0-6)"))

    # Player 2 Input
    else:
        selection = int(input("Player 2 Make your Selection (0-6)"))

    turn += 1
    turn = turn % 2 