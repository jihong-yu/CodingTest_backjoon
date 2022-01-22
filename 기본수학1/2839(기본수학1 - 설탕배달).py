n = int(input())
count = []  # 개수를 담기 위한 봉지의 개수

for i in range((n // 5) + 1):  # 입력 최대값 5000을 만들 수 있는 5kg그램만 사용할 때의 최대 반복 횟수범위
    for j in range((n // 3) + 1):  # 입력 최대값 5000을 만들 수 있는 3kg그램만 사용할 때의 최대 반복 횟수범위
        if n == 5 * i + 3 * j:  # 입력한 값과 5kg 사용 개수와 3kg 사용 개수의 합이 같을 때
            count.append(i + j)  # 해당 값(봉지의 개수)를 count 배열에 넣어 준다.

if len(count) == 0:  # 만약 만들 수 있는 개수의 조합이 없다면
    print(-1)  # -1 출력
else:  # 있다면
    print(min(count))  # 해당 개수의 최소값 출력
