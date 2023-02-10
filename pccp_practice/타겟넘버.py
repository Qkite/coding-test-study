# 더하거나 빼기
# 20개이하 -> 2^19 -> 1024*512 -> 50만


import numpy as np



def solution(numbers, target):
    def find_target(x):
        return x == target

    bef_cal = [0]
    for iter in range(len(numbers)):
        aft_cal = [0]*(2*len(bef_cal))
        for bef_num_iter in range(len(bef_cal)):
            aft_cal[bef_num_iter*2] = bef_cal[bef_num_iter] -numbers[iter]
            aft_cal[(bef_num_iter*2 +1)] =bef_cal[bef_num_iter] + numbers[iter]

        bef_cal = aft_cal

    # print(bef_cal)
    # print(np.where(np.array(bef_cal) == target)[0])

    return len(np.where(np.array(bef_cal) == target)[0])


print(solution([1, 1, 1, 1, 1], 3))
