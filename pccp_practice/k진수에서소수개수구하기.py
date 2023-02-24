# 1, 11 시간초과
def solution(n, k):
    answer = 0
    let = ''

    while n:
        let += f'{n % k}'
        n = n // k
    let += f'{n}'
    let = let[::-1]

    for num in let.split('0'):
        if num == '':
            answer += 0
        elif sum([int(num) % x == 0 for x in range(1, int(num) + 1)]) == 2:
            answer += 1

    return answer