import sys


def quick_sort(array):  # 퀵정렬 이용
    if len(array) <= 1:  # 만약 배열의 길이가 1보다 작거나같다면(원소가 1개이하라면)
        return array  # 그 원소를 반환

    pivot = array[0]  # 첫번째 값을 피봇값으로 설정
    tail = array[1:]  # 피봇값을 제외한 배열을 선언

    left_side = [x for x in tail if x <= pivot]  # 피봇값보다 작거나 같은 값을 피봇값을 기준으로 왼쪽에 분할
    right_side = [x for x in tail if x > pivot]  # 피봇값보다 작거나 같은 값을 피봇값을 기준으로 오른쪽에 분할

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)  # 피봇값보다 작거나같은 배열을 정렬 + 피봇값 + 피봇값보다 큰 배열을 정렬


n = int(input())
array = []

for _ in range(n):
    array.append(int(sys.stdin.readline()))  # 반복문마다 입력시간 줄이기

array = quick_sort(array)

for i in range(len(array)):
    sys.stdout.write(str(array[i]) + '\n')  # 반복할때마다 출력빠르게
