# 왜 시간 초과가 나지? 13분 39초

def calculate_max_value(row, col, triangle):

    if row == len(triangle)-1:
        # depth가 1이라는 것은 가장 마지막 숫자들을 본다는 것


        return triangle[row][col]
    else:

        num1 = calculate_max_value(row+1, col, triangle) + triangle[row][col]
        num2 = calculate_max_value(row+1, col+1, triangle) + triangle[row][col]

        # print(num1)
        # print(num2)
        #
        # print(max(num1, num2))

        return max(num1, num2)
        # depth가 2 이상이면 col이 자기랑 같거나 자기보다 1 큰 경우 중에서 최댓값




def solution(triangle):



    answer = calculate_max_value(0, 0, triangle)

    return answer



print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
