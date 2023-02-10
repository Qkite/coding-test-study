import numpy as np


def solution(col_num, row_num, puddles):
    checked = np.array([[0]*(col_num+1)]*(row_num+1))
    checked[1][1] = 1

    # 웅덩이가 있는 곳

    for i, j in puddles:
        checked[j][i] = -1

    for i in range(1, row_num + 1):
        for j in range(1, col_num + 1):
            if checked[i][j] == -1:
                checked[i][j] = 0 # 웅덩이는 갈 수 없음
                continue

            checked[i][j] += (checked[i - 1][j] + checked[i][j - 1]) % 1000000007

    return (checked[row_num][col_num])

