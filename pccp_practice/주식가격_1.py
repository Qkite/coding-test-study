def solution(prices):

    answer = [0]*len(prices)

    for i in range(len(prices)):

        pointer = i
        count = 0
        critical = prices[pointer]
        pointer += 1

        while(pointer < len(prices)):

            if (prices[pointer] >= critical):
                pointer += 1
                count += 1
            else:
                count += 1
                break

        answer[i] = count

    return answer

print(solution([1,2,3,2,3])) # 4, 3, 1, 1, 0
print(solution([1,2,3,4,2,3])) # 5, 4, 2, 1, 1, 0
print(solution([1,2,3,2,1,4,2,3])) # 7, 3, 1, 1, 3, 1, 1, 0

