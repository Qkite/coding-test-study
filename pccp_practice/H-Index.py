# h번 이상 인용된 논문이 h편 이상인 경우의 h의 최댓값
# citations: 1~1000
# H 값은 0~10000

# 정렬된 array의 index를 골랐을 때 그 값이 index+1 보다 작거나 같으면 OK
# 1,1,1,2,2,3,3,3,4,5,5 이면 3번째 숫자가 3보다 작음 OK

# 오름차순으로 정렬하는데에 -> O(N^2) 이어도 가능은 함, 100만 이니까
# H값 구하는 데에 O(N)

# 2분 추가

# 흠...

def solution(citations):
    answer = 0

    citations = sorted(citations)

    for i in range(len(citations)):

        # 개수 -> len(citations) - i
        # 개수와 값 사이 최솟값이 H-INDEX의 후보값들
        value = min(len(citations) - i, citations[i])

        # 거기에서 최댓값을 구함
        answer = max(answer, value)


    return answer



print(solution([3, 0, 6, 1, 5]))
print(solution([1,1,1,2,2,3,3,3,4,5,5]))

