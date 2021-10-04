x, y, w, h = map(int, input().split())

maxWidth = w - x
minWidth = x - 0

maxHeight = h - y
minHeight = y - 0

print(min(maxWidth,maxHeight,minHeight,minWidth))