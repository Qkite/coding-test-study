# 가능한 연산
# (1) n을 더한다
# (2) 2 또는 3을 곱한다
# DFS와 비슷

# 시간초과 문제 해결

def solution(x, y, n):
    answer = 0
    bef_cal = [x]
    aft_cal = []

    finish_cal = False
    while(finish_cal == False):
        answer += 1
        for bef_num in bef_cal:
            aft_cal.append(bef_num + n)
            aft_cal.append(bef_num*2)
            aft_cal.append(bef_num*3)

        count = 0
        for aft_num in aft_cal:
            if aft_num == y:
                finish_cal = True
            elif aft_num > y:
                count += 1

        if(count == len(aft_cal)):
            finish_cal = True
            answer = -1

        bef_cal = aft_cal
        aft_cal = []


    return answer


print(solution(10,40,5))
print(solution(10,40,30))
print(solution(2,5,4))


