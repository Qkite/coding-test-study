# 1개인 경우는 단어 그대로
# 2개 이상인 경우는 앞에 숫자만 붙음
# 길이만 count 하므로 순서는 상관 없음 -> deque를 이용할 필요 X

def get_compression_length(letter, slice_length):
    letter_dict = {}

    for start_index in range(len(letter), slice_length):
        sliced = letter[start_index:start_index + slice_length]
        if sliced in letter_dict.keys():
            letter_dict[sliced] += 1
        else:
            letter_dict[sliced] = 0





def solution(s):

    return final_length