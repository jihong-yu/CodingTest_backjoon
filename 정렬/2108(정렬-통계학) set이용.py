import sys

n = int(input())

array = []

for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    array.append(a)

array2 = set()

array.sort()

for i in range(len(array)):
    array2.add((array.count(array[i]), array[i]))

count = []
for j in array2:
    count.append(j)

array3 = []
for k in count:
    if max(count)[0] == k[0]:
        array3.append(k[1])

array3.sort()
if len(array3) > 1:
    mode = array3[1]
else:
    mode = array3[0]

#print(round(sum(array) / n, 0))
print(f'{sum(array)/n:0.0f}')
print(array[n // 2])
print(mode)
print(max(array) - min(array))