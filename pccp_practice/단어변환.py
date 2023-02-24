# 한개의 알파벳만 바꿀 수 있음
# words에 있는 단어로만 바꿀 수 있음
# target이 words 안에 없으면 변환할 수 없음
# target 값에서 이동하기


def check_one_diff(word1, word2):

    count = 0

    for i in range(len(word1)):
        if(word1[i] != word2[i]):
            count += 1

    if(count == 1):
        return True
    else:
        return False



def solution(begin, target, words):

    change_count = 0

    if(target not in words):
        return change_count


    find = False
    candidates = [target]

    while(find == False):
        new_candidates = []
        for candidate in candidates:
            if(check_one_diff(candidate, begin)):
                find = True
                break


            for word in words:
                if(check_one_diff(word, candidate)):
                    new_candidates.append(word)

        change_count += 1
        print(change_count)

        candidates = new_candidates



    if(change_count > len(words)):
        return 0
    else:
        return change_count



print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))