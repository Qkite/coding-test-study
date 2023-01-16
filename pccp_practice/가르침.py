# anta....tica는 반드시 포함됨 -> a, n, t, i, c 5개는 무조건 알고 있어야 함

# 단어의 개수(N)는 50 이하-> 2^50
# K는 0이상 26이하 -> 5보다 작으면 무조건 결과가 0임
# 5개 숫자를 모두 제거함 -> 0이상 21이하로 줄어듦
# -> 조합의 개수가 최대가 21C10 = 352716 -> 해볼만함
# 352716 * 50 = 1763만

# 전체 set 중에서 숫자 몇개만 고르기 -> 이 숫자 안에 다 들어가는지?


# 시간 초과... ㅠㅠㅠㅠㅠ -> itertools를 이용하지 않고 하는 방법..?


import sys
from itertools import combinations


nums = sys.stdin.readline().split(" ")
word_num = int(nums[0])
letter_num = int(nums[1])

words = [""]*(word_num)
total_word = ""

for i in range(word_num):
    word = sys.stdin.readline().replace("\n", "").replace("a", "").replace("n", "").replace("t", "").replace("i", "").replace("c", "")
    words[i] = words[i] + word
    total_word = total_word + word


print(words)

def max_word_count(total_word, words, letter_num):

    # print(letter_num)

    if (letter_num < 5):
        return 0

    letter_set = set(total_word) # 전체 알파벳

    word_counts = []



    for combi in combinations(letter_set, letter_num-5):

        count = 0

        for word in words:
            # print(combi)
            # print(word)


            if (set(word) & set(combi) == set(word)):
                count += 1


        word_counts.append(count)

    return max(word_counts)


print(max_word_count(total_word, words, letter_num))











