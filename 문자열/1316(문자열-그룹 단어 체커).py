n = int(input())
count = 0
for i in range(n):
    s = input()

    if len(s) == 1:  # s가 만약에 한자리면은 무조건 그룹단어이다.
        count += 1 #따라서 +1 해준다.
    else: #2자리 이상이라면
        for j in range(1, len(s)): #2번째 인덱스부터 마지막 인덱스까지
            if s[j - 1] == s[j]: #문자 두개씩 비교를 해서 만약 같다면
                pass #아무것도 하지않는다.
            elif s[j - 1] in s[j:]: #만약 문자 두개가 다르고 앞의 문자가 뒤 문자부터 마지막 인덱스 안에 또 등장한다면
                break #반복문을 빠져나간다.
            if j == len(s) - 1: #만약 위의 반복문 break없이 다돌고 마지막 인덱스까지 왔다면
                count += 1 #count +1 해준다.

print(count)
