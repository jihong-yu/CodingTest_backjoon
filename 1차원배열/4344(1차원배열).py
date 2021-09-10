c = int(input())

for _ in range(c):
    array = list(map(int, input().split()))

    sum2 = sum(array[1:])  # 합계 출력
    avg = sum2 / array[0]  # 평균 출력
    count = 0

    for i in range(1, array.__len__()):
        if array[i] > avg:
            count += 1

    result = count / array[0] * 100
    #print("%0.3f%%" % result)  # %0.3f <-result라는 실수를 세번째 소수점까지 출력한다는 의미 , %% <- %를 문자로 출력한다는 의미
    print("%.3f" %result) #<- 다음과같이 표현도 가능