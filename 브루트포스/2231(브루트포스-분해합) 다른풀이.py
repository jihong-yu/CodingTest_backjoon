n = int(input())

result = 0

for i in range(1, n + 1):
    a = list(map(int, str(i))) #i가 123 이라면 [1,2,3]으로 리스트에 저장된다.
    result = i + sum(a)
    if result == n:
        print(i)
        break
    if i == n:
        print(0)
