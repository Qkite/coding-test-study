# number: 2~100만이니까 경우의 수가 100만C50만
# rough하게 2^100만 정도가 됨
# combination을 다 돌리면 안됨
# number안에 있는 숫자를 정렬함 -> 순서를 유지해야함
# -> 따로 array 만들어서 정렬하기
# -> 이렇게 하면 안됨...




"""
1) "1924" -> 1,2 제거함

4132 -> 4,3제거

2) "4177252841" -> 6개가 남아 있어야 함
-> 4,1,2,2 제거함
-> 가장 작은 숫자들을 제거하면 1,1,2,2가 제거되어야 함

- 8,7,7,5,4,2,2,1,1
- 문자열 큰 순서대로 index를 적으면 5(X)8(X)'2''2'6(X)'4'6(X)'1''5''8'
-> 5,8,6,6제거
-> 1 뒤에는 2개 -> 문자열 성립X
-> 2 뒤에는 7개 -> 성립O (6개) -> 문자열 자르기
-> 2 뒤에 6개 -> 성립O (5개) -> 문자열 자르기
-> 4 뒤에는 4개 -> 성립O (4개)
-> 6 뒤에 3개 -> 성립O(3개)
-> 1 뒤에 2개 -> 성립 O(2개)

set을 오름차순으로 정렬해서 하기
-> index가 높은 것부터 순서대로 확인 -> 뒤에 충분한 양의 문자열이 있으면
-> 그 값을 옮기고 나머지를 자름
"""


# 리스트가 문자열처럼 변화하지 않는 문제가 발생 -> 문자열에서 특정 값을 찾음

def solution(number, k):
    answer = ""

    need_length = len(number) - k

    set1 = sorted(set([int(number[i]) for i in range(len(number))]), reverse= True)

    while(need_length > 0):
        for i in range(len(set1)):
            # 문자열에서 특정 글자 위치 찾기
            # find는 특정 문자가 존재하지 않으면 -1 출력
            # index는 에러 메시지 출력
            # find를 사용하기
            number_idx = number.find(str(set1[i]))

            if(number_idx == -1):
                pass
            else:

                if(len(number) - number_idx >= need_length):
                    answer += str(set1[i])
                    number = number[(number_idx+1):]

                    need_length -= 1
                    # 하나를 answer에 넣어주었으니 줄여줌
                    break


    return answer



print(solution("1924", 2)) # 94
print(solution("1231234", 3)) # 3234
print(solution("4177252841", 4)) # 775841
print(solution("1234689", 4)) # 689
print(solution("777777777777778", 4)) # 77777777778






