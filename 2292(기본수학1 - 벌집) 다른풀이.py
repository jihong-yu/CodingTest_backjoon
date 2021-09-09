n = int(input())
a = 1
count_six = 1
i = 1

while n > a:
    count_six = 6 * i
    a += count_six
    i += 1

print(i)

