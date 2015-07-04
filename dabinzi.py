from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's seek Dabinzi out! You have six chances before he comes to you."
print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)

target_row = random_row(board)
target_col = random_col(board)


for turn in range(6):
    print "Turn", turn + 1
    guess_row = int(raw_input("Which Row do you think Dabinzi are in:"))
    guess_col = int(raw_input("Which Col do you think Dabinzi are in:"))

    if guess_row == target_row and guess_col == target_col:
        print "Congratulations! You got Dabinzi!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or \
           (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the field."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed Dabinzi!"
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
        print_board(board)
if turn == 5:
    print "Game Over, Dabinzi is coming to you now."
