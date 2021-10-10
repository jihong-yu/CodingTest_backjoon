import sys

n = int(input())

array = [] #좌표를 담을 리스트 선언

for _ in range(n):
    x, y = sys.stdin.readline().split() #입력을 sys로 받는다 단,문자열로 저장됨
    array.append([int(x), int(y)]) #int로 변환하여 array리스트에 리스트형태로 담아준다.(이중 리스트)

# array.sort() #배열 array를 우선 x값을 기준으로 오름차순 정렬을 해준다.
# array.sort(key=lambda a: a[1]) #그 후 배열 array를 y값을 기준으로 오름차순 정렬을 해준다.

array.sort(key=lambda x: (x[1],x[0])) #먼저 배열의 첫번째 원소(x)를 기준으로 오름차순 한다음 y를 기준으로 오름차순 정렬한다.

for i in array:
    print(i[0], i[1])
