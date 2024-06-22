import random

def roll_dice():
    dice = random.randint(1, 6)
    return dice

def panalty():
    # possibilities
    poss = ["safe", "panalty"]
    sq = []
    for i in range(30):
        # 30% to be panalty, 70% to be safe area
        choice = random.choices(poss, weights=(0.7, 0.3))
        sq.append(choice)
    
    # create squares string
    squares = ""
    for s in sq:
        if s == ["safe"]:
            squares += "_"
        else:
            squares += "P"
    return squares

def cur_round(square, posA, posB, panA, panB):
    winner = False
    if square[posA] == "P":
        if not panA:
            # lose next turn
            panA = True
            diceA = 0
        else:
            panA = False
            diceA = roll_dice()
    else:
        diceA = roll_dice()
    
    if square[posB] == "P":
        if not panB:
            # lose next turn
            panB = True
            diceB = 0
        else:
            panB = False
            diceB = roll_dice()
    else:
        diceB = roll_dice()
    
    # update position
    posA += diceA
    posB += diceB

    # winner condition
    if posA >= 29 and posB >= 29:
        winner = "both"
        posA = 29
        posB = 29
    elif posA >= 29:
        winner = "A"
        posA = 29
    elif posB >= 29:
        winner = "B"
        posB = 29
    # generate board    
    board = gen_board(square, posA, posB)
    print_board(board, diceA, diceB)

    return posA, posB, panA, panB, winner

def gen_board(square, posA, posB):
    board = ["_"]*30
    if posA == posB:
        if square[posA] == "P":
            board[posA] = "x"
        else:
            board[posA] = "X"
    else:
        # A
        if square[posA] == "P":
            board[posA] = "a"
        else:
            board[posA] = "A"
        # B
        if square[posB] == "P":
            board[posB] = "b"
        else:
            board[posB] = "B"
    
    return board

def print_board(board, diceA, diceB):
    for p in board:
        print(p, end="")
    print("(A: %d, B: %d)" % (diceA, diceB))

def main():
    # position
    posA, posB = roll_dice(), roll_dice()
    # panalty
    panA, panB = False, False
    square = panalty()
    # first round
    board = gen_board(square, posA, posB)
    print_board(board, posA, posB)

    # continue the game until find winner 
    while (posA < 29 and posB < 29):
        posA, posB, panA, panB, winner = cur_round(square, posA, posB, panA, panB)
    
    # winning messages
    if winner == "both":
        print("\nBoth players win!\n")
    elif winner == "A":
        print("\nPlayer A wins!\n")
    elif winner == "B":
        print("\nPlayer B wins!\n")
    
    # print square
    print(square, "\n")

main()