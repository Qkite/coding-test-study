# https://www.acmicpc.net/problem/16947

# 순환선임을 어떻게 표현하지?
# N개의 리스트를 만듦 -> 각 input에 따라서 업데이트 하기 만약

# 역의 개수와 주어지는 경우의 수는 같음

import sys
import numpy as np
station_num = int(sys.stdin.readline())
in_circular_line = np.array([-1]*station_num)


for i in range(station_num):
    num1, num2 = map(int, sys.stdin.readline().split(" "))

    if in_circular_line[num1-1] == -1:
        in_circular_line[num1-1] = num2
    if in_circular_line[num2-1] == -1:
        in_circular_line[num2 - 1] = num1


    arr1 = np.where(in_circular_line == (num1))[0]
    arr2 = np.where(in_circular_line == (num2))[0]

    print(arr1)
    print(arr2)

    for index in arr1:
        in_circular_line[index] = num2

    for index in arr2:
        in_circular_line[index] = num1

    print(in_circular_line)













