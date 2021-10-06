n, m = map(int, input().split())

inputNumList = list(map(int,input().split())) #입력을 받아 리스트에 저장
sumSet = set() #중복을 허용하지 않는 set자료형 선언(입력받은 숫자 중 3개의 숫자 합을 저장하기 위해)
sumArray = [] #m보다 작거나 같은 원소만 저장하기 위한 리스트 선언


#반복문을 돌면서 3가지 숫자의 합을 구해야하는데 i==j 이거나 j==k이거나 i==k 일때는 중복이므로
#if문을 걸어 그 경우의 수를 제외시켜 준다.
for i in inputNumList: #입력받은 숫자에 접근
    for j in inputNumList[1:]: #입력받은 숫자의 맨앞원소의 바로 뒤에있는 원소부터 접근
        if i == j: #3개의 숫자중 첫번째 원소와 두번째 원소가 같을 때의 경우수는 반복문을 돌지 않는다.
            break
        for k in inputNumList[2:]: #입력받은 숫자의 맨앞원소의 다음 2번째 에있는 원소부터 접근
            if k == j or k == i: #3개의 숫자중 두번째 원소와 세번째 원소가 같을 때 혹은 첫번째와 세번째가 같은 경우수는 반복문을 돌지 않는다.
                break
            sumSet.add(i + j + k) #3가지 숫자의 합을 집합자료형에 대입하면 같은 수는 중복을 제거해준다.

for i in sumSet: #집합자료형을 돌면서
    if i <= m: #만약 원소가 m보다 작거나 같다면
        sumArray.append(i) #리스트에 그값들을 대입해준다.
print(max(sumArray)) #그 중에서 가장 큰 값을 출력

