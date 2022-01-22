T = int(input())

for _ in range(T):
    # 첫 방 번호 저장
    room = 101
    count = 1  # 반복문 횟수를 저장할 count 값 저장
    H, W, N = map(int, input().split())
    while True:

        # 만약 k 값이 N값과 동일 하다면 room을 출력하고 탈출
        if count == N:
            print(room)
            break

        # 방번호를 100씩 증가시킨다.
        room += 100

        # 만약 방 번호를 100으로 나눈 몫이 높이보다 커진다면
        if (room // 100) > H:
            # 방번호를 1층의 다음 번호로 배정해준다.
            room = 100 + (room % 100 + 1)
        # 횟수를 저장할 count 값을 +1 해준다.
        count += 1
