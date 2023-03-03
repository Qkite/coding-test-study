# 실패 어디에서 문제가?

from collections import deque

def solution(bridge_length, weight, truck_weights):
    final_time = 0
    truck_times = [0]*len(truck_weights)


    on_bridges = deque([])

    truck_num_put_on = 0
    truck_num_get_off = 0

    on_bridges.append(truck_weights[truck_num_put_on])
    truck_times[truck_num_put_on] += 1
    final_time += 1
    truck_num_put_on += 1


    while(truck_num_put_on < len(truck_weights)):
        if(sum(on_bridges) + truck_weights[truck_num_put_on] <= weight):
            on_bridges.append(truck_weights[truck_num_put_on])
            truck_num_put_on += 1

            for i in range(truck_num_get_off, truck_num_put_on):
                truck_times[i] += 1
            final_time += 1


            # print(on_bridges)
        else:
            truck_times[truck_num_get_off] += 1
            final_time += 1

            # print(on_bridges)



        if(truck_times[truck_num_get_off] == bridge_length):
            on_bridges.popleft()
            truck_num_get_off += 1

            if(sum(on_bridges) + truck_weights[truck_num_put_on] <= weight):
                on_bridges.append(truck_weights[truck_num_put_on])
                truck_num_put_on += 1



            # print(on_bridges)




        # print(truck_num_put_on)
        # print(truck_num_get_off)

    final_time += (bridge_length - truck_times[-1]) +1
    return final_time


print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))