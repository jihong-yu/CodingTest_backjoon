import math
import sys

a, b, v = map(int, sys.stdin.readline().split())
currentHeight = 0
count = 0

# while True:
#     currentHeight += a
#     count += 1
#     if currentHeight >= v:
#         break
#     currentHeight -= b

# v <= (a-b * count) + a
# (v-a)/(a-b) <= count

print(math.ceil((v-a)/(a-b)+1))
