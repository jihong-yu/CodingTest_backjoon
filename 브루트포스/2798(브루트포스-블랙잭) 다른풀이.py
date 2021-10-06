from itertools import combinations

n, m = map(int, input().split())
card_list = list(map(int, input().split()))
result = 0 #결과값을 저장하기 위한 변수

for i in combinations(card_list, 3): #combinations 함수를 이용하면 파이썬에서 중복을 허용하지 않고 3개를 뽑아준다.
    if sum(i) <= m: #만약 그 3개의 합이 m보다 작거나 같다면
        result = max(result, sum(i)) #그 값을 result값에다 대입하는데 기존에 있던 result값이 크다면 대입하지 않는다.


print(result)
