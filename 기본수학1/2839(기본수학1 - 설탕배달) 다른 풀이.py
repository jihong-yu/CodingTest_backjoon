n = int(input())

count = 0

while n >= 0:  # n>=0보다 크거나 같다면
    if n % 5 == 0:  # n이 5로나누어 떨어지면
        count += (n // 5)  # n을 5로 나눈 몫을 count에 더해준다
        print(count)  # count 출력
        break  # 반복문 빠져나온다. else문 실행 x
    n -= 3  # n이 5로 나누어 떨지지 않으면 3만큼 빼준다.
    count += 1  # 개수에 한번 더해준다.
else:  # n이 0보다 작고 위의 while문에서 반복문을 break로 빠져나오지 못했다면(itreable이 소진되었을 경우)
    print(-1)  # -1출력
