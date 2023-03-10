# 모든 달은 28일까지라고 가정
# 2000년 1월 1일부터 몇일 떨어졌는지를 기준으로 비교



def days_aft_2020(date):

    date_info = date.split(".")
    day = int(date_info[0])*12*28 + int(date_info[1])*28 + int(date_info[2])
    return day



def solution(today, terms, privacies):
    remove_privacy = []


    remain_date_dict = {}

    today_days = days_aft_2020(today)

    for term in terms:
        term_list = term.split(" ")
        remain_date_dict[term_list[0]] = int(term_list[1])*28


    for order in range(len(privacies)):
        privacy_info = privacies[order].split(" ")
        privacy_date = days_aft_2020(privacy_info[0])
        privacy_policy = privacy_info[1]

        if(privacy_date + remain_date_dict[privacy_policy] <= today_days):
            remove_privacy.append(order+1)


    return remove_privacy