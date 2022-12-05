# 음식 개수(scoville): 2이상 100만 이하
# 스코빌 원소 0 이상 100만 이하
# K (스코빌 지수): 10억 이하 -> Long?


# 최솟값 2개를 어떻게 계속 저장할 수 있을지 -> 우선순위 큐
# 섞은 횟수를 return 함
# 시간 초과
# put()과 get()은 O(log n)의 시간 복잡도...

# heapq를 이용하면 더 빨리 동작함 -> 런타임 에러...?



# 마지막이 뭐지...?

from queue import PriorityQueue
import heapq

def solution(scoville, K):

    answer = 0
    # queue = PriorityQueue()
    # heap에서는 scoville을 그대로 이용

    # for i in range(len(scoville)):
        # queue.put(scoville[i]) # O(N)

    heapq.heapify(scoville)


    if(len(scoville) == 1):
        if(heapq.heappop(scoville) < K):
            return -1
        else:
            return answer
    elif (len(scoville) == 0):
        return -1
    else:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        level = min1

    while level < K:
        #queue.put(min1 + 2*min2)
        heapq.heappush(scoville, min1 + 2*min2)

        answer += 1

        #min1 = queue.get()
        #min2 = queue.get()


        if(len(scoville) >=2):
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            level = min1
        elif(len(scoville) == 1):
            if (heapq.heappop(scoville) < K):
                return -1
            else:
                return answer

            # return이 섞는 횟수이므로 answer에 1을 더해주지 않음
        else:
            return -1

        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1], 7))
print(solution([1,44,1,1,1,1,1,1,5], 7))
print(solution([11,44,21,25], 8))
