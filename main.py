# Board Variables
placeholder_piece = " "
board_size = 3
board = [[placeholder_piece for i in range(board_size)] for j in range(board_size)]
row_divider = "_____________"

# Player 1 variables
player_one_piece = 'X'
player_one_turn = True

# Player 2
player_two_piece = 'O'


def print_board(board):
    print(row_divider)
    for row in board:
        row_string = ""
        for pos in row:
            row_string += f'| {pos} '
        row_string += "|"

        print(row_string)
        print(row_divider)


def loop():
    global player_one_turn
    global board

    piece = player_one_piece if player_one_turn else player_two_piece
    player_one_turn = not player_one_turn

    x_move = input("What column would you like to move to? ")
    y_move = input("What row would you like to move to? ")

    try:
        x_move = int(x_move) - 1
        y_move = int(y_move) - 1

        if board[y_move][x_move] is not placeholder_piece:
            raise Exception("Already moved there")

        board[y_move][x_move] = piece
    except:
        print("There is either already a piece there or that is not a valid move.")
        player_one_turn = not player_one_turn
        loop()


def check_win(board, piece):
    # -- horizontal win
    for row in board:
        if row.count(piece) == len(row):
            return True

    # | vertical win
    for i in range(board_size):
        board_slice = []

        for row in board:
            board_slice.append(row[i])

        if board_slice.count(piece) == len(board_slice):
            return True

    # \ diagonal win
    board_slice = []
    for i in range(board_size):
        board_slice.append(board[i][i])

    # / diagonal win
    board_slice = []
    for i in range(board_size):
        board_slice.append(board[i][board_size - (i + 1)])

    if board_slice.count(piece) == len(board_slice):
        return True


# ------------------ ACTUAL RUNNING GAME CODE ------------------
while True:
    loop()

    print_board(board)

    if check_win(board, player_one_piece):
        print("Congrats Player One!")
        break
    elif check_win(board, player_two_piece):
        print("Congrats Player Two!")
        break
