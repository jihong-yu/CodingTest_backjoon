import sys
from collections import Counter

n = int(input())

array = []

for _ in range(n):
    a = int(sys.stdin.readline().rstrip()) #sys로 데이터 입력 받기
    array.append(a)

array.sort() #오름차순 정렬해주기 -> 중앙값 구할 때 필요하며 또한 Counter함수의 most_common()을 사용하기 위해선
# 해당배열 순서대로 해당 숫자와 그 숫자가 등장하는 횟수를 같이 튜플형태로 저장해준다. 따라서 오름차순으로 정렬을 미리 해주어야 문제 풀기가 편하다.

# 최빈값 구하기
def mode(array):
    mode_dict = Counter(array)
    modes = mode_dict.most_common()  # 각 숫자와 등장 횟수를 튜플형식으로 저장(숫자,등장횟수) 원배열에 저장되어있는 순서대로 들어간다.

    if len(modes) > 1:
        if modes[0][1] == modes[1][1]:
            print(modes[1][0])
        else:
            print(modes[0][0])
    else:
        print(modes[0][0])


print(f'{sum(array) / n:0.0f}') #산술평균
print(array[n // 2]) #중앙값
mode(array) #최빈값
print(max(array) - min(array)) #범위
