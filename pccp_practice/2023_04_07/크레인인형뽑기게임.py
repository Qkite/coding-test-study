# 2개가 만남 -> 큐에서 동일한 원소를 발견하면 제거

from collections import deque

def solution(board, moves):
    count = 0

    pointer = [len(board)-1]*len(board)
    # 각 그룹의 위치 [pointer[번호-1]][번호-1]

    basket = deque([])

    for move in moves:
        print("move: " + str(move))
        print(pointer[move-1])
        if(pointer[move-1] >= len(board)):
            pass
        else:
            doll_num = board[pointer[move-1]][move-1]
            print("doll_num: " + str(doll_num))

            if doll_num > 0:
                if(len(basket) == 0):
                    basket.append(doll_num)
                else:
                    if basket[-1] == doll_num:
                        basket.pop()
                        count += 1
                        print(count)

                    else:
                        basket.append(doll_num)
                pointer[move - 1] += 1
                print(pointer[move - 1])


    return count

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))