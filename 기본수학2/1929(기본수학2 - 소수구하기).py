import math

m, n = map(int, input().split())

array = [True for i in range(n + 1)] # 0~n 까지 모두 소수로 우선 정의해준다.(True면 소수)

for i in range(2, int(math.sqrt(n) + 1)): #0,1을 제외하고 2부터 n이 아닌 n의 제곱근 까지만 검사하면 된다.(n의제곱근이후부터는 반복이기 때문)
    if array[i] == True: #만약 i가 소수라면
        j = 2 # i에 곱해줄 j를 2부터 선언
        while i * j <= n: # i* j 가 n보다 작거나 같을 때 까지
            array[i * j] = False #모두 소수가 아님으로 False로 바꿔준다.
            j += 1 #j를 1씩 증가

if m == 1:  # m이 만약 1이라면 2로 바꾸어준다.(1은 소수가 아니기 때문)
    m += 1  # 이러한 작업을 안할 경우 m이 1일 경우 1도 출력이 되기 때문이다.
for i in range(m,n+1): #m부터 n까지 i로 돈다
    if array[i]: #만약 i가 소수라면
        print(i) #그 i를 출력