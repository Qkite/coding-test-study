# anta....tica는 반드시 포함됨 -> a, n, t, i, c 5개는 무조건 알고 있어야 함

# 시간 초과....?




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


# print(words)

def can_read_words(data, learned, letter_set):
   count = 0
   for word in data:
      can_read = 1
      for letter in word:
         if learned[letter_set.index(letter)] == 0:
            can_read = 0
            break
      if can_read == 1:
         count += 1
   return count



def max_word_count(total_word, words, letter_num):

    # print(letter_num)

    answer = 0

    if (letter_num < 5):
        return 0

    letter_set = list(set(total_word)) # abcdef

    learned = [0]*len(letter_set) # 010101


    for combi in combinations(letter_set, letter_num-5):
        count = 0
        for letter in combi:
            learned[letter_set.index(letter)] = 1

        count = can_read_words(words, learned, letter_set)

        if count > answer:
            answer = count

        for letter in combi:
            learned[letter_set.index(letter)] = 0

    return answer



print(max_word_count(total_word, words, letter_num))











