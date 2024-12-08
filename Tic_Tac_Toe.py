import random


def grid(board):
    print("┌───┬───┬───┐")
    print(f"| {board[0]} | {board[1]} | {board[2]} | ")
    print("├───┼───┼───┤")
    print(f"| {board[3]} | {board[4]} | {board[5]} | ")
    print("├───┼───┼───┤")
    print(f"| {board[6]} | {board[7]} | {board[8]} | ")
    print('└───┴───┴───┘')


def player_move(board):
    while True:
        try:
            pl_move = int(input("Enter your move, a number between 0 and 8: "))
            if pl_move in range(9):
                if board[pl_move] == " ":
                    return pl_move
                else:
                    print("This position is already taken. Enter a new move.")
            else:
                print("Please enter a valid number. The given number is out of range.")
        except(ValueError, IndexError):
            print("Please enter a valid input. Enter a number between 0 and 8.")


def computer_move(board):
    cp_move = [j for j in range(0, 9) if board[j] == " "]
    computer_choice = random.choice(cp_move)
    return computer_choice


def update_board(board, move, player):
    board[move] = player


def check_winner(board):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None


def again():
    while True:
        choice_for_again = input("Do you want to play again? ^_~\n (Yes/No)?  ").upper()
        if choice_for_again == "YES":
            play_game()
        elif choice_for_again == "NO":
            print("It was great to play with you. Thank you for playing. Byee (●'◡'●)")
            break
        else:
            print("Please enter a valid choice either yes or no.")


def player_choice():
    while True:
        current_player = input("What symbol do you want to choose?\n (X/O)? ").upper()
        if current_player in ["X", "O"]:
            return current_player
        else:
            print('''Please enter a valid value either "X" or "O" ''')


def play_game():
    board = [" " for i in range(0, 9)]
    current_player = player_choice()
    computer_player = "O" if current_player == "X" else "X"
    player_turn = True
    for turn in range(9):
        grid(board)
        if player_turn:
            move = player_move(board)
        else:
            move = computer_move(board)
            print(f"Computer chooses move: {move}")

        update_board(board, move, current_player if player_turn else computer_player)
        winner = check_winner(board)
        if winner:
            grid(board)
            print(f"Player {winner} wins!")
            return
        player_turn = not player_turn
    grid(board)
    print("It's a draw!")


play_game()
again()
