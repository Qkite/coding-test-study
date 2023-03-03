def solution(s):
    answer = []
    letter_record = {}
    for letter_order in range(len(s)):
        letter = s[letter_order]
        if(letter in letter_record.keys()):
            answer.append(letter_order - letter_record[letter])
            letter_record[letter] = letter_order

        else:
            answer.append(-1)
            letter_record[letter] = letter_order


    return answer


print(solution("banana"))
print(solution("foobar"))