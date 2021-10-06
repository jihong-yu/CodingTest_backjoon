n = int(input())
weightArray = []

for i in range(n):
    x, y = map(int, input().split())
    weightArray.append([x, y, i])  # 이중리스트 형태로 저장

for i in range(len(weightArray)):  # 이중리스트의 각 리스트에 접근
    rank = 1  # 순위 변수 1로 초기화
    for j in range(len(weightArray)):  # 이중리스트의 각 리스트에 접근(비교대상)
        if weightArray[i][0] < weightArray[j][0] and weightArray[i][1] < weightArray[j][1]:  # 만약 첫번째 사람의 체중과 키가 다른사람의 체중과 키보다 작다면
            rank += 1  # 랭크를 +1 해준다.
    weightArray[i][2] = rank #해당 랭크 값을 리스트에 같이 저장

#랭크 순위대로 정렬
weightArray.sort(key= lambda weightArray:weightArray[2])

#랭크 순위대로 출력(몸무게 출력)
for i in weightArray:
    print(i[0],end=" ")