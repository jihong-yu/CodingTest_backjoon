import math

r = int(input())

uclid = r * r * math.pi
taxi = r * r * 2

#f-string을 이용하여 출력
print(f'{uclid:0.6f}')
print(f'{taxi:0.6f}')

#round함수 이용하여 출력
print(round(uclid,6))
print(round(taxi,6))