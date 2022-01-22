array = []  # k층의 n호를 표기하기 위해 이차원 리스트 선언
temp = []  # 이차원 리스트에 각층의 사람수를 담을 1차원 리스트 선언
for i in range(15):  # 0~14층까지 돈다
    for j in range(14):  # 1호 ~ 14호 까지 (단, 인덱스를 가독성을 위해 0~13으로 해준다.)
        if i == 0:  # 만약 0층이라면
            temp += [j + 1]  # 사람수를 그 호수에 맞게 넣어준다.
        else:  # 1층 이상이라면
            temp += [sum(array[i - 1][0:j + 1])]  # 아래층의 j호 까지의 사람수를 더해준다.
    array.append(temp)  # 그 temp 값을 이차원 리스트에 넣어준다.
    temp = []  # temp 값을 다시 빈 리스트로 초기화

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    print(array[k][n - 1])
