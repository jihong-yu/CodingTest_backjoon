t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    widthCount = 0  # 호텔방의 폭에서 몇번째 방에 들어가야 하는지 즉, 정답이 402호면 2 , 1203호면 3 을 찾는 변수
    heightCount = 0  # 호텔방의 층에서 몇번째 방에 들어가야 하는지 즉, 정답이 402호면 4 , 1203 호면 12를 찾는 변수
    for i in range(1, w + 1):  # 호텔방의 폭만큼 반복문을 돈다
        if h * i >= n:  # 만약 높이 * i 가 n번째 보다 크거나 같다면
            widthCount = i  # 그때의 i는 가로폭에서의 방번호가 되고
            heightCount = n - (h * (i - 1))  # i에서 -1을 해준 값에 높이값을 곱하여 그것을 n번째 손님의 수에서 빼주면 세로높이의 방 번호가 된다.
            break  # 그리고 반복문을 빠져 나간다.
    result = heightCount * 100 + i  # 방번호를 높이의 번호에서는 100을 곱해주면 되고 가로 폭의 방번호는 그냥 더해주면 된다.
    print(result)
