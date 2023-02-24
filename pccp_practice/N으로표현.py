# 1, 11, 111, 1111, ...
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.


# 121 = 11*11 = (55/5)*(55*5)
# 110+11 = 55+55+55/5

# 1, 11, 111 -> 다 모아서 +1 -> 있으면 +1
# (5+55+555)/5

# 5, 55, 555

# 32000까지 -> 11111, NNNNN 까지
# 1,5,8 실패...?

# 22분 13초
def solution(N, number):


    num_dict1 = {}
    num_dict2 = {}
    digit_list = [11111, 1111, 111, 11, 1]

    for i in digit_list:
        num_dict1[N * i] = number//(N*i)
        number = number%(N*i)
        num_dict2[i] = number//(i)
        number = number % (i)


    print(num_dict1)
    print(num_dict2)

    num1 = num_dict1[N * 11111] * 5 + num_dict1[N * 1111] * 4 + num_dict1[N * 111] * 3 + num_dict1[N * 11] * 2 + num_dict1[N * 1] * 1
    num2 = num_dict2[11111] * 5 + num_dict2[1111] * 4 + num_dict2[111] * 3 + num_dict2[11] * 2 + num_dict2[1] * 1


    if N == 1:
        if num1 + num2 <= 8:
            return num1 + num2
        else: return -1

    else:
        if(num2 == 0):
            if num1 <= 8:
                return num1
            else: return -1
        else:

            if (num1+num2+1) <= 8:
                return num1 + num2 + 1
            else: return -1



print(solution(5, 12))
print(solution(2, 11))
print(solution(5, 1))


