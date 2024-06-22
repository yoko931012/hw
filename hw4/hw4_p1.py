import random
import time

def show_board(board):
    print("     a   b   c   d   e   f   g   h   i")
    for i in range(9):
        print("   " + "+---"*9 + "+")
        print(" %d " %(i+1), end="")
        for j in range(9):
            print("| " + board[i][j] + " ", end="")
        print("|")
    print("   " + "+---"*9 + "+")

def first_input(board, pos, dir):
    # x, y-axis is opposite to the statement
    p2 = int(ord(pos[0]) - 96)
    p1 = int(pos[1])

    mine_free = [str(p1)+str(p2)]

    # traverse every direction
    for x, y in dir:
        coor_x = p1 + x
        coor_y = p2 + y
        if 0 <= coor_x <= 9 and 0 <= coor_y <= 9:
            mine_free.append(str(coor_x) + str(coor_y))
    
    return mine_free


def generate_mines(mine_free, dir):
    mines = []
    while len(mines) < 10:
        # randomize the position of mines
        mine = str(random.randint(1, 9)) + str(random.randint(1, 9))
        # avoid mine free position
        if mine not in mines and mine not in mine_free:
            mines.append(mine)
    
    # initialize board with answers
    board_ans = [["0"]*9 for i in range(9)]
    for p in mines:
        p1 = int(p[0])
        p2 = int(p[1])
        # set up mines
        board_ans[p1-1][p2-1] = "X"
    
    for i in range(9):
        for j in range(9):
            sum_mines = 0
            # skip the mine position
            if board_ans[i][j] == "X":
                continue
            # finish the answer board
            for dir_x, dir_y in dir:
                coor_x = i + dir_x
                coor_y = j + dir_y
                if 0 <= coor_x < 9 and 0 <= coor_y < 9:
                    if board_ans[coor_x][coor_y] == "X":
                        sum_mines += 1
            # replace total mines to initial value
            board_ans[i][j] = str(sum_mines)
    return mines, board_ans
   
def display_status(pos, board, board_ans, dir, GameOver):
    p2 = int(ord(pos[0]) - 97)
    p1 = int(pos[1]) - 1
    
    # input position out of the board
    if p1 > 9 or p2 > 9:
        show_board(board)
        print("\nInvalid cell. Enter the column followed by the row \
(ex: a5). to add or remove a flag, add 'f' to the cell (ex: a5f) \n")
        return board

    # flag case  
    if board[p1][p2] == "F":
        show_board(board)
        print("\nThere is a flag there")
    
    # step on mines
    elif board_ans[p1][p2] == "X":
        print("Game over \n")
        show_board(board_ans)
        GameOver = True

    # valid input
    elif board[p1][p2] == " ":
        coor = [[p1, p2]]
        while len(coor):
            p1 = coor[0][0]
            p2 = coor[0][1]
            if board_ans[p1][p2] == "0":
                for x, y in dir:
                    coor_x = p1 + x
                    coor_y = p2 + y
                    if 0 <= coor_x < 9 and 0 <= coor_y < 9:
                        if board[coor_x][coor_y] == " ":
                            coor.append([coor_x, coor_y])

            board[p1][p2] = board_ans[p1][p2]
            del coor[0]
        show_board(board)

    # shown case
    else:
        show_board(board)
        print("\nThe cell is already shown.")

    return board, GameOver

def flag(pos, board):
    p2 = int(ord(pos[0]) - 97)
    p1 = int(pos[1]) - 1
    # flag
    p3 = pos[2]
    if board[p1][p2] == " ":
        board[p1][p2] = "F"
    elif board[p1][p2] == "F":
        board[p1][p2] = " "
    else:
        show_board(board)
        print("\nCannot put a flag there")
        return board

    show_board(board)
    return board

def main():
    # record time
    start_time = time.time()
    GameOver = False

    # direction coordinate
    dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    # initialize board
    board = [[" "]*9 for i in range(9)]
    show_board(board)

    print("\nEnter the column followed by the row (ex: a5). To add or remove a flag, \
add 'f' to the cell (ex: a5f). Type 'help' to show this message again. \n")

    pos = input("Enter the cell (10 mines left): ")
    print("\n")
    # create mine free area
    mine_free = first_input(board, pos, dir)
    mines, board_ans = generate_mines(mine_free, dir)
    # update board
    board, GameOver = display_status(pos, board, board_ans, dir, GameOver)

    sum_flag = 0

    while True:
        # mine number
        mine = 10 - sum_flag

        pos = input("\nEnter the cell (%d mines left): " %mine)
        print()
        if len(pos) == 2:
            board, GameOver = display_status(pos, board, board_ans, dir, GameOver)
        if len(pos) == 3:
            board = flag(pos, board)
        if pos == "help":
            show_board(board)
            print("\nEnter the column followed by the row (ex: a5). To add or remove a flag,\
    add 'f' to the cell (ex: a5f).")
        
        # calculate flag number
        sum_flag = 0
        flag_to_mines = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == "F":
                    sum_flag += 1
                    if board_ans[i][j] == "X":
                        flag_to_mines += 1

        # wining condition
        if sum_flag == flag_to_mines == 10:
            GameOver = True
            end_time = time.time()
            dur = end_time - start_time
            # calculate time using
            min = dur // 60
            sec = dur % 60
            print("\nYou won. It took you %d minutes and %d seconds. \n" % (min, sec))
            show_board(board_ans)

        if GameOver:
            break

# execute main function
main()
while True:
    PlayAgain = input("\nPlay again? (y/n): ")
    if PlayAgain == "y":
        main()
    else:
        break
