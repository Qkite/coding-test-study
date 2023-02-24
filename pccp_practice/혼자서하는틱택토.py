# O 다음 X
# -> O가 1개 더 많거나 O와 X의 개수가 같아야 함

# 3개 연결되는 경우는 stop
# -> 3개가 연결되는 경우가 1개만 있어야 함

# 정상이면 1, 그렇지 않으면 0

# 51.9 -> 어느 부분을 보완?


import numpy as np

def solution(board):

    o_count = 0
    x_count = 0

    o_check_board = np.array([[False]*3]*3)
    x_check_board = np.array([[False]*3]*3)



    for row in range(3):
        o_count += board[row].count("O")
        x_count += board[row].count("X")
        for col in range(3):
            if(board[row][col] == "O"):
                o_check_board[row][col] = True
            elif (board[row][col] == "X"):
                x_check_board[row][col] = True


    if(x_count > o_count):
        return 0
    if(o_count > x_count+1):
        return 0

    # print(x_check_board)
    # print(o_check_board)

    o_bingo = False
    x_bingo = False


    for trial in range(3):
        if(sum(x_check_board[:][trial] == True) == 3):
            x_bingo = True
        if(sum(x_check_board[trial][:]== True) == 3):
            x_bingo = True
        if(sum(o_check_board[:][trial]== True) == 3):
            o_bingo = True

        if(sum(o_check_board[trial][:]== True) == 3):
            o_bingo = True

    if((x_check_board[0][0]== True) and (x_check_board[1][1]== True) and (x_check_board[2][2]== True)):
        x_bingo = True
    if((o_check_board[0][0]== True) and (o_check_board[1][1]== True) and (o_check_board[2][2]== True)):
        o_bingo = True



    if(o_bingo == True) and (x_bingo == True):
        return 0
    return 1



print(solution(["O.X", ".O.", "..X"]))
print(solution(["OOO", "...", "XXX"]))
print(solution(["...", ".X.", "..."]))
print(solution(["...", "...", "..."]))
