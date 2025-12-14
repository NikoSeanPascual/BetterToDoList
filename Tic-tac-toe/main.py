player = 'X'
enemy = 'O'
empty_spaces = ' '


def board():
    return [[empty_spaces for _ in range(3)] for _ in range(3)]


def make_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")


def check_winner(board, you):
    for i in range(3):
        if all([board[i][j] == you for j in range(3)]) or \
                all([board[j][i] == you for j in range(3)]):
            return True

    if board[0][0] == you and board[1][1] == you and board[2][2] == you:
        return True
    if board[0][2] == you and board[1][1] == you and board[2][0] == you:
        return True

    return False


def check_the_board(board):
    for row in board:
        if empty_spaces in row:
            return False
    return True


def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, player):
        return -10 + depth
    if check_winner(board, enemy):
        return 10 - depth
    if check_the_board(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == empty_spaces:
                    board[i][j] = enemy
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = empty_spaces
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == empty_spaces:
                    board[i][j] = player
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = empty_spaces
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


def get_best_move(board):
    best_move = None
    best_value = float('-inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == empty_spaces:
                board[i][j] = enemy
                move_value = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = empty_spaces
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move


def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row col) [0-2]: ").split())
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == empty_spaces:
                    board[row][col] = player
                    break
                else:
                    print("This spot is already taken. Try again, you blind AHH PLAYER")
            else:
                print("Invalid input. Please enter numbers between 0 and 2 for both row and column....IS IT THAT HARD TO UNDERSTAND😞😞😞")
        except ValueError:
            print("Invalid input. Please enter TWO INTEGERS between 0 and 2... is there something wrong with your brain 🥀🥀")


def print_game_result(board, winner):
    make_board(board)
    if winner == player:
        print("Congratulations,I am so impress that you won 🎉🎉🥳!")
    elif winner == enemy:
        print("AI wins! YOU SUCK, just quit at this point 💔💔")
    else:
        print("It's a draw! I dare you to play again...")


def play_again():
    while True:
        play_again_input = input("Do you want to play again (DON'T BE A CHICKEN)? (y/n): ").lower()
        if play_again_input == 'y':
            return True
        elif play_again_input == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n' it's not that difficult 😡😡")


def main():
    while True:
        boarding = board()
        print("Welcome to TicTacToe with an AI opponent 🔥🔥!")
        print("You are 'X' and the AI is 'O'.")
        print("Enter your move as 'row col' (e.g., 1 1 for the center spot).")

        while True:
            make_board(boarding)

            if check_the_board(boarding):
                print_game_result(boarding, None)
                break

            player_move(boarding)

            if check_winner(boarding, player):
                print_game_result(boarding, player)
                break

            if check_the_board(boarding):
                print_game_result(boarding, None)
                break

            print("AI is making its move...")
            ai_move = get_best_move(boarding)
            boarding[ai_move[0]][ai_move[1]] = enemy

            if check_winner(boarding, enemy):
                print_game_result(boarding, enemy)
                break

        if not play_again():
            print("Thank you for playing YOU CHICKEN! Goodbye!")
            break


if __name__ == "__main__":
    main()
