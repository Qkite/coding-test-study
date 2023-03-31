# 화살의 개수가 같으면 어피치가 점수를 받음
# 가장 큰 점수차 -> 어피치가 쏜 것에서 딱 1점 차이가 나면 됨

# 재귀함수가 안 걸리는 문제
def cal_max_score(n, need, idx, win_or_not):

    if(idx == 10):
        return 0, win_or_not
    if(idx<0):
        return 0, win_or_not

    if n-need[idx] < 0:
        return cal_max_score(n, need, idx+1, win_or_not)
    else:
        new_win_or_not = win_or_not[idx]
        new_win_or_not[idx] = True
        if(cal_max_score(n, need, idx+1, win_or_not)[0] >= 10-idx + cal_max_score(n-need[idx], need, idx+1, new_win_or_not)[0]):
            return cal_max_score(n, need, idx+1, win_or_not)
        else:
            return 10-idx + cal_max_score(n-need[idx], need, idx+1, new_win_or_not)[0], new_win_or_not


def solution(n, info):
    needs = []
    for i in info:
        needs.append(i+1) # 해당 점수를 얻으려면 쏘아야하는 화살의 개수들

    # needs를 충족할 떄 가장 큰 점수를 가진다 -> 큰 점수차를 가진다.

    win_or_not = [False]*11

    score, win_or_not_result = cal_max_score(n, needs, 10, win_or_not)

    # 1부터 10 사이 합이 무조건 55 -> score가 28이상이면 이긴 것
    # 28보다 작으면 [-1] return

    result = [0]*11

    print(score)

    if (score < 28):
        return [-1]
    else:
        for idx in range(len(win_or_not_result)):
            if win_or_not_result[idx]:
                result[idx] = needs[idx]
                n -= needs[idx]


        if(n>0):
            for rev_idx in range(len(win_or_not_result), 0, -1):
                if win_or_not_result[rev_idx-1]:
                    result[rev_idx-1] += n

        return result




print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
