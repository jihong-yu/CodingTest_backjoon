n = int(input())
input_num = list(map(int, input().split()))
count = 0 #소수 개수 세기
error = 0 #에러 유무 (0이면 소수, 1이면 소수아님)

for i in input_num: #inputnum 리스트의 각 원소 꺼내기
    for j in range(2, i): #각각의 원소 i마다 2 부터 (i-1)까지 수로 i를 나누기
        if i % j == 0:  #본인 i이외의 수로 나눠서 나머지가 0이라면 소수가 아님
            error += 1 #그럴 경우 에러 추가
            break #반복문 탈출
    if error == 0 and i != 1: #만약 에러도 없고 i도 1이 아니라면
        count += 1 #소수의 개수 추가
    error = 0 #다시 error값을 0으로 초기화

print(count) #소수개수 출력