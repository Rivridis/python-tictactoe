import numpy as np
import random
import time

# -- Setting up arrays --
board = np.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])
print(board)

# -- Taking input --
coin = input("Choose : [X/O]").upper()
cc = ""

# -- Checking input Validity --
if coin not in ["X", "O"]:
    print("Invalid Input")
    exit()

# -- Setting up computer coin --
if coin == "X":
    cc = "O"
else:
    cc = "X"

# --Check Function--
def Check(board):
    global cc
    global coin
    # -- Coloumn Check --
    for i in board:
        if i.tolist() == [cc, cc, cc]:
            return True
        elif i.tolist() == [coin, coin, coin]:
            return True

    # -- Row Check --
    for i in range(0, 3):
        J = board[:,i]
        if J.tolist() == [cc, cc, cc]:
            return True
        elif J.tolist() == [coin, coin, coin]:
            return True

    # -- Digonal left check --
    if [board[0, 0], board[1, 1], board[2, 2]] == [cc, cc, cc]:
        return True
    elif [board[0, 0], board[1, 1], board[2, 2]] == [coin, coin, coin]:
        return True


    # -- Digonal right check --
    if [board[0, 2], board[1, 1], board[2, 0]] == [cc, cc, cc]:
        return True
    elif [board[0, 2], board[1, 1], board[2, 0]] == [coin, coin, coin]:
        return True
    
    return False



# -- Main Game --
while True:

    # -- User Turn --
    print("User Turn")
    time.sleep(0.5)
    pos1, pos2 = input("Enter Row and Coloumn number")
    pos1 = int(pos1)
    pos2 = int(pos2)
    pos1 -= 1
    pos2 -= 1
    if board[pos1, pos2] == "-":
        board[pos1, pos2] = coin
    else:
        print("Space taken, try again")
        continue
    print(board)

    if Check(board) == True:
        print('The User has won')
        exit()
    time.sleep(1)
    print("Computer's turn")
    time.sleep(0.5)

     # -- Check Tie Condition --
    Ch = False
    for i in board:
        for j in i:
            if str(j) == "-":
                Ch = True

    if Ch == False:
        print('Tie')
        break

    # -- Computer Turn --
    while True:
        p1 = random.randint(0, 2)
        p2 = random.randint(0, 2)
        if board[p1, p2] == "-":
            board[p1, p2] = cc
            break
    print(board)

    # -- Check Results --
    if Check(board) == True:
        print('The computer has won')
        exit()
    time.sleep(1)

     # -- Check Tie Condition --
    Ch = False
    for i in board:
        for j in i:
            if str(j) == "-":
                Ch = True

    if Ch == False:
        print('Tie')
        break


