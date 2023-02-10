import sys

def calculate_move_count(start, end):

    if start == end:
        return 0

    if (start - end == 1) or (start - end == -1):
        return 1

    if end % 2 == 0:
        return 1 + calculate_move_count(start, end//2)

    # 2배 이동하는 것을 생각하기 -> 홀수인 경우 1과 짝수로 나누기
    if (end % 2 == 1):
        return 1 + calculate_move_count(start, end - 1)




input = sys.stdin.readline().replace("\n", "").split(" ")
start = int(input[0])
end = int(input[1])

print(calculate_move_count(start, end))