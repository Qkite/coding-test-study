
## 1. numpy 이용하기

import numpy as np

def solution(arr):
    arr1 = np.array(arr)
    if (len(arr) <= 1):
        return [-1]
    else:
        arr1 = np.delete(arr1, np.where(arr1== min(arr1))[0])
        return arr1.tolist()


print(solution([115,2,3,11,1]))


def solution1(arr):
    if (len(arr) <= 1):
        return [-1]
    else:
        temp = arr[0]
        # temp에 가장 작은 수가 들어갈 수 있도록 함
        for i in range(1,len(arr)):
            if (temp > arr[i]):
                temp = arr[i]
        arr.remove(temp)
        print(temp)
        return arr


print(solution1([115,2,3,11,1]))