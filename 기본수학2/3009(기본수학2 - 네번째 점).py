# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())
# x4, y4 = 0, 0

# # x축
# if x1 == x2:
#     x4 = x3
# elif x2 == x3:
#     x4 = x1
# elif x1 == x3:
#     x4 = x2
#
# # y축
# if y1 == y2:
#     y4 = y3
# elif y2 == y3:
#     y4 = y1
# elif y1 == y3:
#     y4 = y2

# print(x4, y4)

xArray = []
yArray = []
for _ in range(3):
    x, y = map(int, input().split())
    xArray.append(x), yArray.append(y)

for i in range(3):
    if xArray.count(xArray[i]) == 1:
        resultX = xArray[i]
    if yArray.count(yArray[i]) == 1:
        resultY = yArray[i]
print(resultX,resultY)

