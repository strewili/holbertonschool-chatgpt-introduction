#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position. Please enter numbers from 0 to 2.")
                continue

            if board[row][col] == " ":
                board[row][col] = player

                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print("Player " + winner + " wins!")
                    break

                if board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break

                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

tic_tac_toe()
