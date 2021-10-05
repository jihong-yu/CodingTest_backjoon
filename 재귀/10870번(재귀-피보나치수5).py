n = int(input())

# def pivo(n: int) -> int:
#     if n >= 2:  # n이 2이상일 때만
#         return pivo(n - 2) + pivo(n - 1)  # 피보나치 수열 실행
#     else:  # n이 1이하일때는
#         return n  # 해당값 출력



pivonacci = [0, 1]  # 피보나치수열을 위한 배열선언 및 0,1 값은 미리 초기화
for i in range(2, n + 1): #2부터 n까지 반복문 돌기
    num = pivonacci[i - 2] + pivonacci[i - 1] #n번째 피보나치수열을 구하기 위해서 n-2번째와 n-1번째의 값 더하기
    pivonacci.append(num) #해당 n번째 피보나치 수열값을 배열에 추가

print(pivonacci[n])

# print(pivo(n))
