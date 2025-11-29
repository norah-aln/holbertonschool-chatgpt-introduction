#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input(f"Enter row (0,1,2) for player {player}: "))
            col = int(input(f"Enter column (0,1,2) for player {player}: "))
        except ValueError:
            print("Invalid input. Numbers only.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid position.")
            continue

        if board[row][col] != " ":
            print("Spot taken.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print_board(board)
            print("Draw!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()

