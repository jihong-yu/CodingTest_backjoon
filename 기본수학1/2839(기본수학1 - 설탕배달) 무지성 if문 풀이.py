N = int(input())

count3 = 0  # 3kg 봉지의수
count5 = 0  # 5kg 봉지의 수

result = 0

# 만약 N이 5로 나누어 떨어지지 않는다면
if N % 5 != 0:
    # 입력받은 N kg을 최대 5kg 봉지와 최대3kg로 어디까지 나눌 수 있는지를 구한다.
    for i in range(1, (N // 5) + 1):
        if (N - (5 * i)) % 3 == 0:
            count5 = i
            count3 = ((N - (5 * i)) // 3)
            result = count5 + count3

    if N % 3 == 0:  # 만약 N이 3으로 나누어 떨어진다면
        if result < (N // 3) and result != 0:  # result값이 0이 아니고 3kg봉지만으로 채우는 경우의 수보다 작다면
            print(result)  # 그 5kg 3kg 봉지의 합을 출력
        else:  # 만약 result값이 0이 거나 3kg봉지만으로 구성한 개수가 3,5를 섞었을때의 개수보다 작을 경우
            print(N // 3)
    else:  # 만약 N이 3으로 나누어 떨어지지 않는다면
        if result == 0:  # result 값이 초기값이라는 것은 5로도 나누어 떨어지지 않고 3으로도 나누어 떨어지지 않았다는 뜻이므로
            print(-1)  # -1을  출력
        else:  # result값이 0이 아닌데 여기 조건까지 왔다면
            print(result)  # result 값을 출력
else:  # 만약 N이 5로 나누어 떨어진다면
    print(N // 5)