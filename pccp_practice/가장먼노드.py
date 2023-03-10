# 노드 2만개 이하
# 간선 5만개 이하
# 1번에서 가장 멀리 떨어진 노드가 무엇인지

import numpy as np


def solution(n, edges):
    distance_array = np.array([[False] * (n + 1)] * (n + 1))

    for edge in edges:
        distance_array[edge[0]][edge[1]] = True
        distance_array[edge[1]][edge[0]] = True

    while (sum(distance_array[1]) < (n - 1)):
        for col in range(1, n + 1):
            if (distance_array[i][col]):
                for row in range(1, n + 1):
                    if (distance_array[row][col]):

    print(distance_array)
    print()

    return 1;


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])