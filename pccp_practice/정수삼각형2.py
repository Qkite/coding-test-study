import copy

def solution(triangle):

    # 층의 개수 = 숫자 개수

    max_nums = [0]*len(triangle)
    print(max_nums)

    max_nums[0] = triangle[0][0]
    print(max_nums)


    for i in range(1,len(triangle)):

        max_nums1 = copy.copy(max_nums)


        max_nums[0] = max_nums1[0] + triangle[i][0]
        max_nums[i] = max_nums1[i-1] + triangle[i][i]

        for j in range(1, i):
            max_nums[j] = triangle[i][j] + max(max_nums1[j-1], max_nums1[j])

        print(max_nums)


    return max(max_nums)


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

