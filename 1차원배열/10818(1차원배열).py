n = int(input())

for _ in range(n):
    array = list(map(str, input()))
    sum = 0
    c = 1
    for i in array:
        if i =="O":
            sum += c
            c += 1
        else:
            c = 1
    print(sum)
