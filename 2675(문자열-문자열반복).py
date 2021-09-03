t = int(input())

for _ in range(t):
    info = list(map(str, input().split()))
    n = int(info[0])
    s = list(str(info[1]))

    for i in s:
        print(i * int(n), end="")
    print()

for _ in range(t):

    n,s = input().split() #공백으로 두개의 인자를 구분받아 각각의 원소에 대입
    text =""
    for i in s: # 파이썬은 str형도 iterable객체이기 때문에 리스트에 담지않아도 바로 반복문에서 각각의 원소(문자)에 접근할 수 있다.("abc" -> "a","b","c")
        text += (i * int(n))
    print(text)
