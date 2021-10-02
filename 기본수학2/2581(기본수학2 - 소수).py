m = int(input()) 
n = int(input())
error = 0 #소수 유무(0 이면 소수, 1이면 소수x) 
array = [] #소수들을 저장할 배열 선언
 
for i in range(m, n + 1): #m부터 n까지 각원소 i에 접근
    for j in range(2, i): #각 원소 i마다 2부터i-1 까지의 수로 나누어 준다.
        if i % j == 0: #만약 i가 2부터 i-1까지의 수로 나누어 떨어진다면 
            error += 1 #소수가 아님
            break #반복문을 빠져나온다.
    if error == 0 and i != 1: #만약 반복문 후에 소수가 맞고 그것이 1이 아닌경우
        array.append(i) #해당 원소를 배열에 추가해준다.
    error = 0 #다시 에러값을 0으로 초기화

if len(array) == 0: #만약 배열에 아무 값이 없다면(소수가 없다면)
    print(-1) #-1을 출력
else: #소수가 있다면
    print(sum(array)) #배열의 합 출력
    print(min(array)) #배열의 최솟값 출력