# 순서대로, 사용한 카드는 다시 사용할 수 없음
# 사용하지 않고 넘어갈 수 없음


def solution(cards1, cards2, goal):
    pointer1 = 0
    pointer2 = 0
    can_make = True

    for word in goal:


        if (pointer1 < len(cards1)) and (cards1[pointer1] == word):
            pointer1 += 1
        elif (pointer2 < len(cards2)) and (cards2[pointer2] == word):
            pointer2 += 1
        else:
            can_make = False
            break

    if(can_make):
        return 'Yes'
    else:
        return 'No'


print(solution(["i", "water", "drink"], ["want", "to"],["i", "want", "to", "drink", "water"]))
