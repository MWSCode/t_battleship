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
    if board[row][col] == "S":
        return True
    elif board[row][col] == "~":
        return False
    elif board[row][col] == "X":
        return "a"
    elif board[row][col] == ".":
        return "a"

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
    global player_hit, computer_hit, ships
    player_hit = 0
    computer_hit = 0
    
    empty_board = create_board()
    players_board = place_ships(empty_board)
    computers_board_invisible = place_ships(empty_board)
    computers_board = list(empty_board)     # computer's visible board
    #print("computers_board_invisible:")
    #print_board(computers_board_invisible)
    
    while True:
        print("Player's Board:")
        print_board(players_board)
        print("Computer's Board:")
        print_board(computers_board)
        print(f"Your score: {player_hit}")
        
        row, col = get_player_input()
        if row == "q":
            print("Bye!")
            break
        else:
            pass
            
        # check if player has hit a ship:
        hit_result = check_hit(computers_board_invisible, row-1, col-1)
        if hit_result == True:
            print("You hit!")
            # mark the areas hit
            computers_board[row-1][col-1] = "X"
            computers_board_invisible[row-1][col-1] = "X"
            player_hit += 1
        elif hit_result == "a":
            print("They had already shot that spot!")
        else:
            print("You missed!")
            # mark the missed areas
            computers_board[row-1][col-1] = "."
            computers_board_invisible[row-1][col-1] = "."
        if player_hit == ships:
            print("Congratulations! You have sunk all your ships and won!")
            #break
            user_input = input("Enter R to restart the game, or Q to quit: ")
            response = game_start_end(user_input)
            if response == False:
                print("Bye!")
                break
        
        # check if computer has hit a ship:
        computer_hit_result, players_board = computer_hit_func(players_board)
        if computer_hit_result == True:
            print("The computer sank your ship!")
            computer_hit += 1
        else:
            print("The computer missed")
            
        if computer_hit == ships:
            print("The computer has sunk all your ships and won!")
            user_input = input("Enter R to restart the game, or Q to quit: ")
            response = game_start_end(user_input)
            if response == False:
                print("Bye!")
                break

game_start_end("")