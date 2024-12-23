"""
TERMINAL BATTLESHIP v1

help resource links:


"""

from random import randint

# variables:
ships = 4       # number of ships
size = [4, 5]   # board-size: row, column
player_hit = 0
computer_hit = 0

# print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

# create a board
def create_board():
    # create the Board:
    board = [["~"] * size[1] for x in range(0, size[0])]
    return board

# fill the board with ships:
def place_ships(board):
    pass

# get player inputs
def get_player_input():
    pass

def check_hit(board, row, col):
    pass

def computer_hit_func(board):
    pass

def game_start_end(u_input):
    print("test")

def game_play():
    pass

print_board(create_board())
