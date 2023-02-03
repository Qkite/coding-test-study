

# fees 이용해서 계산하기

import math

def solution(fees, records):

    result = []

    car_dict = {}
    at_parking_lot = {}


    for record in records:

        car_num = record[6:10]
        time = int(record[:2])*60 + int(record[3:5])

        if(car_num in at_parking_lot.keys()):
            if(car_num in car_dict.keys()):
                car_dict[car_num] += time - at_parking_lot[car_num]
            else:
                car_dict[car_num] = time - at_parking_lot[car_num]

            at_parking_lot.pop(car_num)
        else:
            at_parking_lot[car_num] = time


    # 출차 기록이 없는 경우
    # 23시 59분 ->
    for num, minute in at_parking_lot.items():
        if (num in car_dict.keys()):
            car_dict[num] += 23*60 + 59 - minute
        else:
            car_dict[num] = 23*60 + 59 - minute



    for (num, minute) in sorted(car_dict.items()):
        price = fees[1] + math.ceil(max(minute - fees[0], 0) / fees[2])*fees[3]

        result.append(price)


    return result



print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))