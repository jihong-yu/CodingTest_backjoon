n = int(input())
a = 1
i = 1
if n == 1:
    print(1)
else:
    while True:
        if n <= a + 6 * i:
            print(i+1)
            break
        a += 6 * i
        i += 1



