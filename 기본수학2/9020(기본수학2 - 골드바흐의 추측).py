import math

# 에라토스테네스의 체를 이용하여 10000까지 존재하는 소수 구해놓기
m = 10000 #문제에서 제공한 n의 범위

array1 = [True for _ in range(m + 1)] #소수를 판별(True == 소수)을 위한 리스트 선언
array1[0], array1[1] = False, False #0,1은 소수가 아니기에 False로 선언


for i in range(2, int(math.sqrt(m) + 1)): #2부터 m(10000)의 제곱근까지 반복문을 돈다.
    if array1[i]: #만약 i가 소수라면
        j = 2 #i에 곱해줄 j 선언
        while i * j <= m: #i * j 가 10000(m)이하일때까지
            array1[i * j] = False #해당 i * j 값들을 모두 소수가 아닌것으로 바꿔준다
            j += 1 #j값 증가

t = int(input()) #테스트케이스 수 입력
for _ in range(t): #테스트케이스 만큼 돈다
    n = int(input()) #골드바희의 추측을 위한 짝수 입력

    a = n // 2 #n을 2로 나누어준 몫을 대입
    b = n // 2 #n을 2로 나누어준 몫을 대입

    while True: #무한반복
        if array1[a] and array1[b]: #만약 a 와 b가 위에서 구한 리스트에 존재하는 소수라면
            print(a, b) #그 해당소수를 출력한후
            break #반복문을 빠져나온다.
        a -= 1 #a를 -1씩 줄여나가면서 체크
        b += 1 #b를 +1씩 줄여나가면서 체크