
import sys

length, goal = map(int, sys.stdin.readline().split(" "))
nums = list(map(int, sys.stdin.readline().split(" ")))

counts = 0

left_idx = -1
right_idx = -1
sum = 0

while (True):
    if(right_idx < length -1):
        if(sum < goal):
            right_idx += 1
            sum += nums[right_idx]
        else:
            left_idx += 1
            sum -= nums[left_idx]
    else:
        left_idx += 1
        sum -= nums[left_idx]

    if(sum == goal):
        counts += 1

    if (right_idx >= length -1) and (left_idx >= length -1):
        break

print(counts)






