a = int(input())
b = int(input())
c = int(input())

product = a*b*c

result = list(str(product)) # a*b*c 의 곱을 문자열로 바꿔 list형으로 저장

for i in range(10):
    print(result.count(str(i))) #result내부 문자열 i 의 개수를 샌다.