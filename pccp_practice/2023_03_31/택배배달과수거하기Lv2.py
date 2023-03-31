# n은 물류 창고 개수
# 한도
# 배달과 픽업이 완료되었으면 표시를 할 수 있는 리스트 만들기


from collections import deque

def solution(cap, n, deliveries, pickups):
    distance = 0

    deliveries_deque = deque([])
    pickups_deque = deque([])

    for i in range(len(deliveries)):
        count = deliveries[i]
        while count>0:
            deliveries_deque.append(i+1)
            count -= 1

    for j in range(len(pickups)):
        count = pickups[j]
        while count > 0:
            pickups_deque.append(j+1)
            count -= 1


    while(len(deliveries_deque)>0 or len(pickups_deque)>0):
        if(len(deliveries_deque) == 0):
            distance += 2*pickups_deque[-1]
            for a in range(cap):
                if(len(pickups_deque)>0):
                    pickups_deque.pop()
        elif (len(pickups_deque)==0):
            distance += 2*deliveries_deque[-1]
            for a in range(cap):
                if(len(deliveries_deque)>0):
                    deliveries_deque.pop()
        else:
            distance += 2*max(deliveries_deque[-1], pickups_deque[-1])
            for a in range(cap):
                if(len(deliveries_deque)>0):
                    deliveries_deque.pop()
                if(len(pickups_deque)>0):
                    pickups_deque.pop()


    return distance



print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))