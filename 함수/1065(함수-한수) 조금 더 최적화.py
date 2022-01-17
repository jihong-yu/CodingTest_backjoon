N = int(input())
count = 0  # 정답을 출력할 count 개수 출력

for i in range(10, N + 1):  # 10부터 N 까지 반복문을 돈다.
    temp = set()  # 중복을 허용하지 않는 Set 자료형 선언
    for j in range(len(str(i)) - 1):  # i를 문자열로 변경하여 그 길이의 -1 까지 돈다.
        temp.add(int(str(i)[j]) - int(str(i)[j + 1]))  # temp에 각 숫자 자리수의 차를 대입해준다.(ex) 123 일경우 2-1=1 , 3-2=1, 2개가 대입)
    if len(temp) == 1:  # 만약 temp의 길이가 1이라면
        count += 1  # 각 자리수가 등차수열 이므로 count값 1증가

if N < 10:  # N이 10보다 작다면 반드시 등차수열이므로 그 값을 출력
    print(N)
else:  # 만약 10보다 크다면
    print(count + 9)  # 1~9 는 등차수열 이므로 그 값을 count 값에 더해준다.
