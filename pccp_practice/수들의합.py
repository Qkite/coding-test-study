# 시간 초과

import sys

factors = sys.stdin.readline().split(" ")
length = int(factors[0])
goal = int(factors[1])
nums = list(map(int, sys.stdin.readline().split(" ")))

counts = 0

for i in range(length):
    pointer = i
    sum = 0

    while(pointer < length):
        sum += nums[pointer]
        if(sum == goal):
            counts += 1
            break
        elif (sum > goal):
            break
        else:
            pointer += 1

print(counts)






