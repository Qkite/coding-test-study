def solution(s):
    s = s[2:-2]

    print(s)

    lists = s.split("},{")

    answer = []

    letter_dict = {}
    for letters in lists:
        letter_list = letters.split(",")
        for letter in letter_list:
            if int(letter) in letter_dict.keys():
                letter_dict[int(letter)] += 1
            else:
                letter_dict[int(letter)] = 1

    # 값을 기준으로 내림차순 sorting
    letter_dict_sorted = sorted(letter_dict.items(),reverse=True, key=lambda item: item[1])

    for key, value in letter_dict_sorted:
        answer.append(key)



    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

