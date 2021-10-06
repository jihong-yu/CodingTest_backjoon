n = int(input())
weightArray = []

for i in range(n):
    x, y = map(int, input().split())
    weightArray.append([x, y]) #이중리스트 형태로 저장

for i in weightArray: #이중리스트의 각 리스트에 접근
    rank = 1 #순위 변수 1로 초기화
    for j in weightArray: #이중리스트의 각 리스트에 접근(비교대상)
        if i[0] < j[0] and i[1] < j[1]: #만약 첫번째 사람의 체중과 키가 다른사람의 체중과 키보다 작다면
            rank += 1 #랭크를 +1 해준다.
    print(rank, end=" ")
