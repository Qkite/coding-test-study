# price(1+2+3+...+count)가 최종 가격
# 1+2+3+...+count -> 반복문
# or n(n+1)/2
# 돈이 부족하지 않으면 0 return

def solution(price, money, count):
    total_price = int(price*count*(count+1)/2)

    if total_price>money:
        return total_price - money
    else:
        return 0


    # return max(total_price - money, 0) -> 시간 오래 걸림


print(solution(3,20,4))