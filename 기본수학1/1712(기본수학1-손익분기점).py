import sys

a,b,c = map(int,sys.stdin.readline().split())
count = 0
if b >= c:
    count -= 1
else:
    # while True:
    #     count += 1
    #     if a + b * count < c * count:
    #         break
    count = a//(c-b) + 1 #int(a/(c-b)) +1 도 가능

print(count)

