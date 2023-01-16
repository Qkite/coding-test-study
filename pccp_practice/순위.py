# 선수 100명 이하
# 경기결과 4500개 이하 -> 100C2
# 순위를 결정할 수 있다
# 5명 중 5등은 강한 사람이 앞에 있다
# 자기를 key로 가지고 자기보다 약한 사람의 리스트를 value로 가짐

# 100*100 리스트
# 자기자신이면 0, 크면 1, 작으면 -1
# 0이 1개인 경우만 선택하기

import numpy as np
def calculate_rate(n, results):
    arr = np.array([[0]*n]*n)

    # 행을 기준으로 보자

    for result in results:
        win = result[0]
        lose = result[1]


        arr[win-1][lose-1] = 1
        arr[lose-1][win-1] = -1

        for i in range(n):
            arr[i]

        print(arr)

        print(sum(arr == 0))



    return 2

calculate_rate(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])

arr1 = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
arr1[3][0] = 0
print(arr1)


