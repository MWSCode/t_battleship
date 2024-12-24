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
    i = 0
    while i < ships:
        row = randint(0, size[0]-1)   # min, max
        col = randint(0, size[1]-1)
        # print(row,", ",col,", i:",i)
        if board[row][col] == "S":
            continue
        else:
            board[row][col] = "S"
            i += 1
        
    return board

# get player inputs
def get_player_input():
    while True:
        row = input(f"Enter ROW (1-{size[0]}) or Q to quit: ")
        if row == "q":
            return "q", ""
        try:
            row = int(row)      # accepts only numbers
        except ValueError: # 
            print(f"Choose a number from 1 to {size[0]} !: ")
        else:
            if row in range(1, size[0]+1): # 
                break
            else:
                print("Out of range. Try again.")

    while True:
        col = input(f"Enter COLUMN (1-{size[1]}) or Q to quit: ")
        if col == "q":
            return "q", ""
        try:
            col = int(col)
        except ValueError:
            print(f"Choose a number from 1 to {size[1]} !: ")
        else:
            if col in range(1, size[1]+1): # 
                break
            else:
                print("Out of range. Try again.")
    
    return row, col

def check_hit(board, row, col):
    pass

def computer_hit_func(board):
    pass

def game_start_end(u_input):
    if u_input == "q" or u_input == "Q":
        return False
    elif  u_input == "r" or u_input == "R":
        game_play()
    elif  u_input == "":       # for the first run
        print("*********************************************")
        print("       Welcome to TERMINAL BATTLESHIP        ")
        print(f"  Each Battlefield has {size[0]} Rows and {size[1]} Columns  ")
        print(f"         There are {ships} ships to sink           ")
        print("     Row and column 1 start at top-left      ")
        print("*********************************************")
        #user_input = input("Press any key to start the game or Q to quit: ")
        user_input = input("Enter 1 to start the game, or Q to quit: ")
        if user_input == "q" or user_input == "Q":
            return False
        else:
            game_play()
    else:
        return False

def game_play():
    pass

empty_board = create_board()
board = place_ships(empty_board)
print_board(board)