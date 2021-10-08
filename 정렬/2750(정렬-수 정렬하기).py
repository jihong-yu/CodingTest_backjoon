n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

# 버블 정렬
for i in range(len(array) - 1):
    for j in range(len(array) - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

# 삽입 정렬
for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 앞쪽은 이미 정렬이 되어있기 때문에 자기보다 작은 데이터 만나면 그자리에서 멈춤
            break

for i in range(len(array)):
    print(array[i])
