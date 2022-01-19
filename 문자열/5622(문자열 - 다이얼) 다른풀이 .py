s = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
temp = 0  # 총 전화를 위해 걸리는 시간 0으로 설정

for i in range(s.__len__()):  # 입력한 문자열의 길이만큼
    for j in dial:  # dial의 리스트에 있는 한 원소씩 뺀다
        if s[i] in j:  # 입력한 문자열의 각각의 문자가 다이얼에 포함이 되어있다면
            temp += dial.index(j) + 3  # 그다이얼의 인덱스 +3 만큼 시간을 더한다.

print(temp)
