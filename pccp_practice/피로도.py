from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for permutation in permutations(dungeons, len(dungeons)):
        tmp = k
        count = 0

        for need, spend in permutation:
            if tmp >= need:
                tmp -= spend
                count += 1
        answer = max(answer, count)
    return answer