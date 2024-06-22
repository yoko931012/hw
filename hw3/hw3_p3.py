# show board function
def show_chart(pos):
    for i in range(6):
        print("+---"*7 + "+")
        for j in range(7):
            print("| " + pos[i][j] + " ", end="")
            if j == 6:
                print("|")
    print("+---"*7 + "+")
    for i in range(7):
        print("  "+ str(i) + " ", end="")
    print("")

# going to the next round
def next_round(rou, isValid):
    # check if the operation is valid 
    isValid = False
    if rou % 2 == 1:
        player = "X"
    else:
        player = "O"
    
    # input the operation, which column
    col = input(" Player "+ player +" >> ")
    if not col.isdigit():
        print("Invalid input, try again [0-6].")
        isValid = False
        return isValid
    elif col.isdigit() and (int(col)>6 or int(col)<0):
        print("Out of range, try again [0-6].")
        isValid = False
        return isValid
    else:
        col = int(col)

    i = 5
    while i >= 0:
        if pos[i][col] == " ":
            pos[i][col] = player
            isValid = True
            break
        else:
            i-=1

    # column is full
    if not isValid:
        print("This column is full. Try another column.")

    return isValid

def find_winner(pos):
    # decide who is winner
    winner = " "
    # vertical
    for i in range(7):
        for j in range(3, 6):
            if pos[j][i] == pos[j-1][i] == pos[j-2][i] == pos[j-3][i] and pos[j][i]!=" ":
                winner = pos[j][i]
                pos[j][i] = pos[j][i].lower()
                pos[j-1][i] = pos[j-1][i].lower()
                pos[j-2][i] = pos[j-2][i].lower()
                pos[j-3][i] = pos[j-3][i].lower()
                
    # horizontal
    for i in range(6):
        for j in range(3, 7):
            if pos[i][j].lower() == pos[i][j-1].lower() == pos[i][j-2].lower() == pos[i][j-3].lower() and pos[i][j]!=" ":
                winner = pos[i][j]
                pos[i][j] = pos[i][j].lower()
                pos[i][j-1] = pos[i][j-1].lower()
                pos[i][j-2] = pos[i][j-2].lower()
                pos[i][j-3] = pos[i][j-3].lower()
    
    # diagonal, first direction
    for i in range(3, 6):
        for j in range(3, 7):
            if pos[i][j].lower() == pos[i-1][j-1].lower() == pos[i-2][j-2].lower() == pos[i-3][j-3].lower() and \
                pos[i][j] != " ":
                winner = pos[i][j]
                pos[i][j] = pos[i][j].lower()
                pos[i-1][j-1] = pos[i-1][j-1].lower()
                pos[i-2][j-2] = pos[i-2][j-2].lower()
                pos[i-3][j-3] = pos[i-3][j-3].lower()
    
    # diagonal, second direction
    for i in range(3, 6):
        for j in range(4):
            if pos[i][j].lower() == pos[i-1][j+1].lower() == pos[i-2][j+2].lower() == pos[i-3][j+3].lower() and \
            pos[i][j] != " ":
                winner = pos[i][j]
                pos[i][j] = pos[i][j].lower()
                pos[i-1][j+1] = pos[i-1][j+1].lower()
                pos[i-2][j+2] = pos[i-2][j+2].lower()
                pos[i-3][j+3] = pos[i-3][j+3].lower()

    return winner   


# round
rou = 1
isValid = True
# initialize position matrix
pos = [[" "]*7 for i in range(6)]

while True:
    if isValid:
        show_chart(pos)
    isValid = next_round(rou, isValid)
    
    if isValid:
        rou += 1
    
    winner = find_winner(pos)
    if winner != " ":
        # the uppercase of pos
        board = [[ele.upper() for ele in row] for row in pos]
        show_chart(board)
        show_chart(pos)

        # print the winner
        print("Winner: ", winner)
        break
    
    # check if the checkerboard is full
    isSpace = False
    for i in range(6): 
        for j in range(7):
            if pos[i][j] == " ":
                isSpace = True
    if not isSpace:
        show_chart(pos)
        print("Drew")
        break