import sys

n = int(input())

array = []

#입력받기
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    array.append(a)

array.sort() #배열 정렬

#최빈값 함수
def mode(array):
    if len(array) == 1:
        print(array[0])
        return

    array2 = []  # 입력 받은 배열의 숫자와 등장횟수를 저장할 리스트 선언( [[등장횟수,해당 인덱스]] 로 저장 )

# 여기서 부터 Counter함수의 most_common() 내장함수 직접구현
    if len(array) != 1:  # 만약 입력받은 배열의 길이가 1이 아니라면
        for i in range(len(array)):  # 해당배열의 길이만큼 돈다
            if i == (len(array) - 1):  # 만약 i가 마지막 인덱스라면
                array2.append([array.count(array[i]), array[i]])  # 리스트에 추가 [[등장횟수,해당 인덱스]]
            elif array[i] != array[i + 1]:  # 만약 i가 마지막인덱스가 아니라면 앞 뒤의 배열의 숫자를 비교해서 다르다면
                array2.append([array.count(array[i]), array[i]])  # 리스트에 추가 [[등장횟수,해당 인덱스]]

    array2.sort(key=lambda a: a[0], reverse=True) #순서를 많이 등장한 순서로 리스트의 정렬을 변경해준다.
# 여기 까지 Counter함수의 most_common() 내장함수 직접구현

    if len(array2) > 1:
        if array2[0][0] == array2[1][0]:
            print(array2[1][1])
        else:
            print(array2[0][1])
    else:
        print(array2[0][1])

print(f'{sum(array) / n:0.0f}') #산술평균
print(array[n // 2]) #중앙값
mode(array) #최빈값
print(max(array) - min(array)) #범위
