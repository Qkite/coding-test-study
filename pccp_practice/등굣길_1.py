import numpy as np

def solution(col_num, row_num, puddles):
    checked = np.array([[0]*(col_num+1)]*(row_num+1))


    for row in range(1, row_num+1):
        for col in range(1, col_num+1):
            if row == 1 and col == 1:
                checked[row][col] = 1
            elif [row, col] in puddles:
                checked[row][col] = 0
            else:
                checked[row][col] = (checked[row-1][col] + checked[row][col-1])% 1000000007

    print(checked)

    return int(checked[row_num][col_num])

print(solution(4, 3, [[2,2]]))


