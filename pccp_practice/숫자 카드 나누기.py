# A의 최대 공약수이고 B의 소수
# B의 최대 공약수 이고 A에 소수
# 길이가 50만개 -> 50만 + 50만 -> 100만


# 최대 공약수 구하기
def gcd(a, b):

    if a< b:
        temp = a
        a = b
        b = temp


    while b > 0:
        a, b = b, a % b
    return a




def cal_GCD_and_Prime(array1, array2):

    GCD = array1[0]
    can_not_divide = True

    for i in range(1, len(array1)):
        GCD =gcd(GCD, array1[i])

    print("GCD: ", GCD)

    for i in range(len(array2)):
        if(array2[i] % GCD ==0):
            can_not_divide = False
            break

    if(can_not_divide):
        return GCD
    else:
        return 0


def solution(arrayA, arrayB):

    return max(cal_GCD_and_Prime(arrayA, arrayB), cal_GCD_and_Prime(arrayB, arrayA))



print(solution([10,20], [5,17]))

