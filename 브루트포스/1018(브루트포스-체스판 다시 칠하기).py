n, m = map(int, input().split())  # 행 * 열
array = []
result = []

for _ in range(n):
    a = input()
    b = list(map(str, a)) #문자열을 한단위씩 쪼개서 리스트에 대입("abc" -> "a","b","c")
    array.append(b)

for a in range(n-7): # 8 * 8의 개수가 나오는 경우의 수는 행의길이 - 7 * 열의길이 - 7 의 개수만큼 나온다.
    for b in range(m-7): # 8 * 8의 개수가 나오는 경우의 수는 행의길이 - 7 * 열의길이 - 7 의 개수만큼 나온다.
        countW = 0
        countB = 0
        for i in range(a, a+8):  # 행
            for j in range(b, b+8):  # 열
                if (i + j) % 2 == 0: #두 행과열의 인덱스를 더한값이 짝수라면 색은 다 일치해야됨
                    if array[i][j] != "W":  # (i + j) % 2 == 0위치에서 W를 칠해야하는 경우
                        countW += 1 
                    if array[i][j] != "B":  # (i + j) % 2 == 0위치에서 B를 칠해야하는 경우
                        countB += 1
                elif (i + j) % 2 != 0: #두 행과열의 인덱스를 더한값이 홀수라면 색은 다 일치해야됨
                    if array[i][j] != "B":  # 위의 조건 (i + j) % 2 == 0 부분에서 W이기 때문에 (i + j) % 2 != 0 위치에서 B가 아닐 경우 B를 칠해야하는 경우
                        countW += 1
                    if array[i][j] != "W":  # 위의 조건 (i + j) % 2 == 0 부분에서 B이기 때문에 (i + j) % 2 != 0 위치에서 W가 아닐 경우 W를 칠해야하는 경우
                        countB += 1
        result.append(countW) #각 8 * 8 체스판마다  (i + j) % 2 == 0위치에서 W를 색칠한 횟수 입력((i + j) % 2 != 0 위치에서는 B색칠)
        result.append(countB) #각 8 * 8 체스판마다  (i + j) % 2 == 0위치에서 B를 색칠한 횟수 입력((i + j) % 2 != 0 위치에서는 W색칠)

print(min(result)) #색칠한 횟수중 최소값 출력