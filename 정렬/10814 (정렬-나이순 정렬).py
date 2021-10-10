n = int(input())

array = []
for i in range(n):
    age, name = map(str, input().split())
    array.append((int(age), name))

array.sort(key=lambda array:array[0]) #나이순대로만 정렬
#array.sort() 를 하면 안된다.


for i in array:
    print(i[0], i[1])
