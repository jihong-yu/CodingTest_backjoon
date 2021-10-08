import sys

n = int(input())
array = [0] * 10001

for i in range(n):
    n = int(sys.stdin.readline())
    array[n] += 1  # 각 데이터에 해당하는 인덱스 값 증가(== 인덱스가 해당 숫자 이고 들어간 값이 해당숫자의 개수 ex) array[2] = 3 이면 숫자 2가 3번 있다는 뜻)

for i in range(len(array)):  # array의 길이만큼
    for j in range(array[i]):  # 해당 숫자(i)의 개수만큼
        sys.stdout.write(str(i) + "\n")  # 출력
