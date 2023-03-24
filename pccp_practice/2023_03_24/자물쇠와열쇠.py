# 회전, 이동 가능
# 바깥쪽은 어떻든 상관없지만 lock의 영역 내에서는
# 모든 홈이 다 채워져야 함


# 완전 탐색


def rotate_90(m):
    N = len(m)
    rotated = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            rotated[c][N-1-r] = m[r][c]
    return rotated


def check(new_array, lock_length):
    result = True
    for row in range(lock_length):
        for col in range(lock_length):
            if new_array[row][col] != 1:
                result = False
    return result



def solution(key, lock):

    rotated_lock = rotate_90(lock)

    for rotate_num in range(4):
        for i in range(len(lock)):
            new_array = [[0]*(len(key) + len(lock)) for _ in range(len(key) + len(lock))]
            new_array[]



        # key를 이동시켜서 lock에 맞는지 확인



    answer = True
    return answer
