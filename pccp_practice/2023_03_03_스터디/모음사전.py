# A -> E -> I -> O -> U
# 최대 5개 까지

# 첫 글자
# A: 0*5^4 +1~ 1*5^4
# E: 1*5^4 +1 ~ 2*5^4
# I: 2*5^4 +1 ~ 3*5^4
# O: 3*5^4 +1 ~ 4*5^4
# U: 4*5^4 +1 ~ 5*5^4

# AA: 2

# 앞에서 부터 계산하기


def solution(word):
    answer = 0

    for letter_num in range(len(word)):
        answer += 1

        if(word[letter_num] == 'A'):
            answer += 0
        elif (word[letter_num] == 'E'):
            answer += 1*(5**(4-letter_num))
        elif (word[letter_num] == 'I'):
            answer += 2*(5**(4-letter_num))
        elif (word[letter_num] == 'O'):
            answer += 3*(5**(4-letter_num))
        elif (word[letter_num] == 'U'):
            answer += 4*(5**(4-letter_num))

        print(word)
        print(answer)

    return answer


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))