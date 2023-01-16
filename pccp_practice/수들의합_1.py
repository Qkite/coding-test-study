# 시간 초과

import sys

length, goal = map(int, sys.stdin.readline().split(" "))
nums = list(map(int, sys.stdin.readline().split(" ")))

counts = 0

for i in range(length):
    sum = 0
    for pointer in range(i, length):
        sum += nums[pointer]
        if(sum == goal):
            counts += 1
            break
        elif (sum > goal):
            break

print(counts)






