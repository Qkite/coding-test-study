def solution(k, tangerines):
    size_and_num = {}
    for tangerine in tangerines:
        if (tangerine in size_and_num.keys()):
            size_and_num[tangerine] += 1
        else:
            size_and_num[tangerine] = 1

    #print(size_and_num)



    answer = 0

    #print("answer: ", answer)

    for size, num in sorted(size_and_num.items(), key=lambda x:x[1], reverse=True):
        answer += 1
        #print("size: ", size)
        k -= num
        if (k<=0):
            break


    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))