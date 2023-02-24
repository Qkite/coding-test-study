# 555 -> 55 * 10 + 5

# 바로 직전까지의 계산을 고려했을 때 이러한 결과가 나옴... ㅠ -> 이전 것을 전부다 계산해주어야 함

print("3"*3)


# 5이면 1,4/ 2,3/ 3,2/ 4,1
def after_cal(N, list1, list2, length):

    aft_list = []

    aft_list.append(int(str(N)*(length+1)))
    aft_list.append(int("1"*(length)))

    for num1 in list1:
        for num2 in list2:
            aft_list.append(num1 + num2)
            aft_list.append(num1 - num2)
            aft_list.append(num2 - num1)
            aft_list.append(num1 * num2)
            if(num2 != 0):
                aft_list.append(num1 / num2)
            if(num1 != 0):
                aft_list.append(num2 / num1)

    return aft_list

def solution(N, number):

    bef_list = [[N]]
    length = 1


    for i in range(1, 9):
        if (number in bef_list[i-1]):
            return length
        else:
            # 2이면 1:  0,0 ->
            # 3이면 2: 0,1/ 1,0 ->
            # 4이면 3: 0,2/ 1,1/ 2,0
            after_list = []
            for j in range((i+1)//2):
                after_list = after_list + after_cal(N, bef_list[j], bef_list[i-j-1], length)


            bef_list.append(after_list)
            length += 1

    return -1

print(solution(5, 12))
print(solution(2, 11))
print(solution(4, 31))







