
"""

"AAAE"는 "A", "AA", "AAA", "AAAA", "AAAAA", "AAAAE", "AAAAI", "AAAAO", "AAAAU"의 다음인 10번째 단어입니다.

-> 흠... I나 E가 나오면 그 이하의 숫자들을 다 더해주어야 함
-> AAA -> AAAE가 되려면 5^1+1 +1


A
AA
AAA -> 3
AAAA -> 4
AAAAA
AAAAE
AAAAI
AAAAO
AAAAU
AAAE -> 10
AAAEA
AAAEE
AAAEI
AAAEO
AAAEU
AAAI -> 16
AAAIA
AAAIE
AAAII
AAAIO
AAAIU
AAAO -> 22
AAAOA
AAAOE
AAAOI
AAAOO
AAAOU
AAAU -> 28
AAAUA
AAAUE
AAAUI
AAAUO
AAAUU
AAE -> 34

5글자 -> 1개: 1
4글자 -> 6개 차이: 1*5+1
3글자 -> 31개 차이: 6*5 +1
2글자 -> 156개 차이: 31*5 +1
1글자 -> 781개 차이: 156*5 + 1
"""


def solution(word):
    answer = 0

    delta = [781, 156, 31, 6, 1]

    for letter_num in range(len(word)):
        answer += 1

        if(word[letter_num] == 'A'):
            answer += 0*delta[letter_num]
        elif (word[letter_num] == 'E'):
            answer += 1*delta[letter_num]
        elif (word[letter_num] == 'I'):
            answer += 2*delta[letter_num]
        elif (word[letter_num] == 'O'):
            answer += 3*delta[letter_num]
        elif (word[letter_num] == 'U'):
            answer += 4*delta[letter_num]

        # print(word)
        # print(answer)

    return answer


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))