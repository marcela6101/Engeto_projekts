"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Marcela Vilášková
email: vilaskova.marcela@seznam.cz
discord: marcela6101
"""
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
first_player = "X"
second_player = "O"
game_running = True
def print_board(board):
    print("+-----+-----+-----+")
    print("|  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "  |")
    print("+-----+-----+-----+")
    print("|  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "  |  ")
    print("+-----+-----+-----+")
    print("|  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  |  ")
    print("+-----+-----+-----+")
def first_player_input(board):
    move = True
    while move:
        inp = int(input("Player X | Please enter your move number: "))

        if inp >= 1 and inp <= 9 and board[inp-1] == " ":
            board[inp-1] = first_player
            move = False
        elif inp >= 10 or inp == 0 or inp is not int:
            print("Wrong move, please play again!")
def second_player_input(board):
    move = True
    while move:
        inp = int(input("Player O | Please enter your move number: "))

        if inp >= 1 and inp <= 9 and board[inp-1] == " ":
            board[inp-1] = second_player
            move = False
        elif inp >= 10 or inp == 0 or inp is not int:
            print("Wrong move, please play again!")
def check_horizontal(board):
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True
def check_row(board):
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[1]
        return True
def check_diagonal(board):
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        return True
def check_draw(board):
    if " " not in board:
        print_board(board)
        print("It is a draw!")
        return True
def game_over(game_running):
    if game_running == False:
        print("Game over")
def cela_hra():
    print("""Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game""")
    first_player = "X"
    second_player = "O"
    game_running = True
    while game_running:
        if check_row(board) or check_horizontal(board) or check_diagonal(board) == True:
            game_over(game_running)
            print_board(board)
            print(f"Congratulations, the player {second_player} WON!")
            break
        else:
            print_board(board)
            first_player_input(board)
            if check_draw(board) == True:
                game_running = False
                game_over(game_running)
                break
            if check_row(board) or check_horizontal(board) or check_diagonal(board) == True:
                game_over(game_running)
                print_board(board)
                print(f"Congratulations, the player {first_player} WON!")
                break
            print_board(board)
            second_player_input(board)
            if check_draw(board) == True:
                game_running = False
                game_over(game_running)
                break
if __name__ == '__main__':
    cela_hra()
