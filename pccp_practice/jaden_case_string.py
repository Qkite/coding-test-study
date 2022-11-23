
# runtime error
"""
def solution(s):
    answer = ""
    inputs = s.split(" ")
    for input in inputs:
        answer += input[0].upper()
        answer += input[1:].lower()
        answer += " "

    # upper 함수: 공백, 숫자는 그대로, 알파벳만 대문자로 변환
    answer = answer[:-1] # 마지막에 오는 공백 제거
    return answer
"""

def solution(s):
    answer = ""
    # 아스키코드 이용하기
    # 어떻게 대문자 자리인지를 확인하지?
    upper_location = True
    for i in range(len(s)):
        code = ord(s[i])
        if upper_location:
            if code >= 97 and code <= 122:
                answer += chr(code - 32)
                upper_location = False
            elif code == 32:
                answer += s[i]
                upper_location = True
            else:
                answer += s[i]
                upper_location = False

        else:
            if code >=65 and code <= 90:
                answer += chr(code + 32)
            elif code == 32:
                answer += s[i]
                upper_location = True
            else:
                answer += s[i]

    return answer



print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution("for  a  the  dd last   week"))