
## 1. numpy 이용하기

import numpy as np

def solution(arr):
    arr1 = np.array(arr)
    if (len(arr) <= 1):
        return np.array([-1])
    else:
        print(min(arr1))
        arr1 = np.delete(arr1, np.where(arr1== min(arr1))[0])
        return arr1


print(solution([115,2,3,11,1]))