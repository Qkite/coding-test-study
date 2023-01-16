import sys
from collections import deque


# 식의 계산은 연산자 우선 순위를 무시하고 앞에서 부터 진행해야 함
# -> Dynamic Programing
# 100개 이하

# number_num = sys.stdin.readline()
# nums = sys.stdin.readline().split(" ")
# numbers = deque([int(x) for x in nums])
# operators = sys.stdin.readline().split(" ")
# operator_nums = [int(x) for x in operators]


# 음... 기록하는걸로 가야하는지?


numbers = deque([3,4,5])
operator_nums = [1,0,1,0]



def cal1(nums, operator_nums):

    sign_change = 0


    if(len(nums) == 2):

        if(operator_nums[0]>0):
            return nums[0] + nums[1]
        elif (operator_nums[1]>0):
            return nums[0] - nums[1]
        elif (operator_nums[2]>0):
            return nums[0] * nums[1]
        elif (operator_nums[3]>0):
            return nums[0] // nums[1]

    elif(len(nums) ==1):
        return nums[0]

    else:

        num1 = nums.popleft()
        num2 = nums.popleft()


        if(num1 < 0):
            left_num = num1*(-1)
            sign_change += 1
        else: left_num = num1



        if(num2 < 0):
            right_num = num2*(-1)
            sign_change += 1
        else: right_num = num2

        results = []

        if operator_nums[0] > 0:
            changed_num = (left_num + right_num) * ((-1)**sign_change)
            operator_nums1 = [operator_nums[0]-1, operator_nums[1], operator_nums[2], operator_nums[3]]



            results.append(cal1(deque([changed_num]) + nums, operator_nums1))

        if operator_nums[1] > 0:
            changed_num = (left_num - right_num) * ((-1)**sign_change)
            operator_nums1 = [operator_nums[0], operator_nums[1]-1, operator_nums[2], operator_nums[3]]

            results.append(cal1(deque([changed_num]) + nums, operator_nums1))


        if operator_nums[2] > 0:
            changed_num = (left_num * right_num) * ((-1)**sign_change)
            operator_nums1 = [operator_nums[0], operator_nums[1], operator_nums[2]-1, operator_nums[3]]

            results.append(cal1(deque([changed_num]) + nums, operator_nums1))

        if operator_nums[3] > 0:
            changed_num = (left_num // right_num) * ((-1)**sign_change)
            operator_nums1 = [operator_nums[0], operator_nums[1], operator_nums[2], operator_nums[3]-1]

            results.append(cal1(deque([changed_num]) + nums, operator_nums1))

        return max(results)


def cal2(nums, operator_nums):

    sign_change = 0


    if(len(nums) == 2):

        if(operator_nums[0]>0):
            return nums[0] + nums[1]
        elif (operator_nums[1]>0):
            return nums[0] - nums[1]
        elif (operator_nums[2]>0):
            return nums[0] * nums[1]
        elif (operator_nums[3]>0):
            return nums[0] // nums[1]

    elif(len(nums) ==1):
        return nums[0]

    else:

        num1 = nums.popleft()
        num2 = nums.popleft()


        if(num1 < 0):
            left_num = num1*(-1)
            sign_change += 1
        else: left_num = num1



        if(num2 < 0):
            right_num = num2*(-1)
            sign_change += 1
        else: right_num = num2

        results = []

        if operator_nums[0] > 0:
            changed_num = (left_num + right_num) * ((-1)**sign_change)
            operator_nums1 = [operator_nums[0]-1, operator_nums[1], operator_nums[2], operator_nums[3]]

            results.append(cal2(deque([changed_num]) + nums, operator_nums1))

        if operator_nums[1] > 0:
            changed_num = (left_num - right_num) * ((-1)**sign_change)
            operator_nums1 = [operator_nums[0], operator_nums[1]-1, operator_nums[2], operator_nums[3]]

            results.append(cal2(deque([changed_num]) + nums, operator_nums1))


        if operator_nums[2] > 0:
            changed_num = (left_num * right_num) * ((-1)**sign_change)
            operator_nums1 = [operator_nums[0], operator_nums[1], operator_nums[2]-1, operator_nums[3]]

            results.append(cal2(deque([changed_num]) + nums, operator_nums1))

        if operator_nums[3] > 0:
            changed_num = (left_num // right_num) * ((-1)**sign_change)
            operator_nums1 = [operator_nums[0], operator_nums[1], operator_nums[2], operator_nums[3]-1]

            results.append(cal2(deque([changed_num]) + nums, operator_nums1))

        return min(results)

print(cal1(numbers, operator_nums))
print(cal2(numbers, operator_nums))







    





