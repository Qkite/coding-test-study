import math

def solution(n):
    after_multiple = n-1
    for divisor in range(2, int(math.sqrt(after_multiple))+1):
        if(after_multiple % divisor ==0):
            return divisor
    return after_multiple


print(solution(10))
print(solution(12))