from collections import deque

def solution(prices):

    answer = [0]*len(prices)

    for i in range(len(prices)):

        stack = deque(prices[i:])
        count = 0
        critical = stack.popleft()

        while(len(stack)>0):
            value = stack.popleft()
            if(value >= critical):
                count += 1
            else:
                count += 1
                break

        answer[i] = count


    # 효율성 테스트 X



    return answer

print(solution([1,2,3,2,3])) # 4, 3, 1, 1, 0
print(solution([1,2,3,4,2,3])) # 5, 4, 2, 1, 1, 0
print(solution([1,2,3,2,1,4,2,3])) # 7, 3, 1, 1, 3, 1, 1, 0

