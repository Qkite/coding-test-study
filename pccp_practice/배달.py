# N: 마을 개수: 50이하
# road: 2000개 이하
# K: 제한시간 - 10000 이하

# 런타임 에러 발생
import numpy as np

def solution(N, road, K):

    time_list = [0]*N
    location = {1}


    # 바로 연결되어있는 경우
    for line in road:
        if line[0] == 1:
            if time_list[line[1]-1] == 0:
                time_list[line[1]-1] = line[2]
            else: time_list[line[1]-1] = min(line[2], time_list[line[1]-1])
            location.add(line[1])
        elif line[1] == 1:
            if time_list[line[0]-1] == 0:
                time_list[line[0]-1] = line[2]
            else: time_list[line[0]-1] = min(line[2], time_list[line[0]-1])
            location.add(line[0])

    # 100개까지만 존재 -> 100번 이내에 다 연결될 것
    for i in range(50):
        for line in road:

            # 동일한 도시들을 이어주는 다른 루트가 있으므로 1과 연결된 도시에서도 반드시 0인지 확인해야 함
            if line[0] in location:
                if time_list[line[1]-1] == 0:
                    time_list[line[1]-1] = time_list[line[0]-1] + line[2]
                    location.add(line[1])
                else:
                    time_list[line[1] - 1] = min(time_list[line[0] - 1] + line[2], time_list[line[1]-1])
                    location.add(line[1])

            if line[1] in location:
                if time_list[line[0]-1] == 0:
                    time_list[line[0]-1] = time_list[line[1]-1] + line[2]
                    location.add(line[0])
                else:
                    time_list[line[0] - 1] = min(time_list[line[1] - 1] + line[2], time_list[line[0]-1])
                    location.add(line[0])



    print(time_list)

    # 1번은 반드시 0시간이 걸림 -> K시간이 넘더라도 count되지 않도록 처리해주어야 한다 -> [1:]

    return N - len(np.where(np.array(time_list[1:]) > K)[0])



print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))
print(solution(7, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1], [1,7,2], [2,7,6]], 4))
print(solution(6, [[1,2,1],[2,1,4],[1,3,2],[3,1,3],[2,3,2],[3,4,3],[4,3,5],[3,5,2],[3,5,3],[5,6,1]], 4))



