array = input()
countInfo = []
result = ""
upperArray = array.upper()  # array문자열을 모두 대문자로 변경

for j in range(ord("A"), ord("Z")+1): #A부터 Z까지  아스키코드 값으로 돌기
    for i in upperArray: #대문자로 변경한 문자열 접근
        if j == ord(i): #대문자로변경한 문자의 각 아스키코드 값이 A-Z의 아스키코드 값과 같다면
            countInfo.append([upperArray.count(i), j]) # 해당하는 아스키코드 값과 그것의 개수를 countInfo 이중 리스트에 저장
            #여기서 이중리스트에 첫번째 값은 항상 sort,max 등의 함수에 사용되기 때문에 count값을 첫번째 원소로 저장
            break #찾았을 경우 중복하지 않기 위해서 반복문을 빠져나온다.

result = chr(max(countInfo)[1]) #count의 값이 가장 큰 이중리스트의 2번째원소인 아스키코드를 다시 문자열로 변경하여 result값에 대입

for k in range(1,countInfo.__len__()):  # 세로크기(행의크기) 여기서 countinfo[0].__len__() 하게되면 열의크기(가로크기) 를 반환한다.
    countInfo.sort(reverse=True) #최댓값이 2개이상인지를 검사하기 위해 정렬수행(Max값이기 때문에 reverse를 주어 내림차순으로 정렬)
    if countInfo[k-1][0] == countInfo[k][0] and countInfo[k-1][0] == max(countInfo)[0] and countInfo[k][0] == max(countInfo)[0]:
        #2개의 원소의 값이 같고 그것이 최댓값과 같으면 최댓값이 2개이상이기 때문에 다음과 같은 조건을 만듬(단, 이조건은 정렬을 해야 만족할 수 있음)
        result = '?' #그럴경우 ?를 입력
        break # 2개의 원소가 이미 최댓값과 같다는 것은 그다음 원소를 탐색할 필요가 없기 때문에 바로 반복문을 빠져나온다.

print(result)
