# 시간초과

def solution(n, left, right):

    num_list = []

    for i in range(n):
        for k in range(i+1):
            num_list.append(i+1)
        for j in range(i+1, n):
            num_list.append(j+1)

    # print(num_list)

    return num_list[left:right+1]

print(solution(3,2,5))