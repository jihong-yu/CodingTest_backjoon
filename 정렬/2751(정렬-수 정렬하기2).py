import sys

n = int(input())
array = []

for _ in range(n):
    array.append(int(sys.stdin.readline()))  # 반복문마다 입력시간 줄이기

array.sort() #내장함수 이용

for i in range(len(array)):
    #print(array[i])
    sys.stdout.write(str(array[i])+'\n') #반복할때마다 출력빠르게
