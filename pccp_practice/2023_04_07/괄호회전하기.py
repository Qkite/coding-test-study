# 올바른 괄호를 찾기
# [[]] 감싸는 경우
# 옆에 있는 경우

from collections import deque

def correct_bracket_sets(s):

    remained = deque([])
    right_brackets = ["}", ")", "]"]


    for letter in s:
        if len(remained) == 0 and letter in right_brackets:
            return False

        if letter == "(" and remained[-1] == ")":
            remained.pop()
        elif letter == "{" and remained[-1] == "}":
            remained.pop()
        elif letter == "[" and remained[-1] == "]":
            remained.pop()

        else: remained.append(letter)

    if len(remained) == 0:
        return True
    else:
        return False











def solution(s):

    count = 0

    for i in range(len(s)):
        s = s[1:] + s[0] # 왼쪽으로 회전하기

        if(correct_bracket_sets(s)):
            count += 1
    return count