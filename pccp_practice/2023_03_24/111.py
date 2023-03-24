import copy


def solution(ability):
    if len(ability) == 1:
        return ability[0][0]
    elif len(ability[0]) == 1:
        return max(ability)
    else:
        datas = []

        for i in range(0, len(ability)):
            new_array = copy.copy(ability)
            del new_array[i]



            datas.append(ability[i][0] + solution(new_array[:][1:]))

        print(datas)

        return max(datas)

print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
print(solution([[20, 30], [30, 20], [20, 30]]))