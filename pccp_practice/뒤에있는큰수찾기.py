def solution(numbers):
    answer = [0]*len(numbers)

    for i in range(len(numbers)-1):

        print(answer)

        for j in range(i+1, len(numbers)):
            if(numbers[i] < numbers[j]):

                answer[i] = numbers[j]

                break
        if(answer[i] == 0):
            answer[i] = -1

    answer[len(numbers)-1] = -1

    return answer

print(solution([2,3,3,5]))
print(solution([9, 1, 5, 3, 6, 2]))