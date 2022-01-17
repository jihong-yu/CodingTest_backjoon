array = [False] * 10036 #9999 일때의 경우의 수를 고려해 10036까지 배열 설정


def solve():
    for i in range(1, 10001):
        if i < 10: #한자리수일때
            array[i + i] = True #각자리수의 합+전체수를 True로 변경
        elif i < 100: #두자리 수일때
            array[i + (i // 10) + (i % 10)] = True #각자리수의 합+전체수를 True로 변경
        elif i < 1000: #세자리 수일때
            array[i + (i // 100) + (i % 100 // 10) + (i % 100 % 10)] = True #각자리수의 합+전체수를 True로 변경
        elif i < 10000: #네자리 수일때
            array[i + (i // 1000) + (i % 1000 // 100) + (i % 1000 % 100 // 10) + (i % 1000 % 100 % 10)] = True #각자리수의 합+전체수를 True로 변경

    for i in range(1, 10001):
        if array[i] == False: #True가 아닌것들은 생성자가 없는 수들이기 때문에 False만 출력
            print(i)

solve()
