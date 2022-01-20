n = int(input())
count = 0
for j in range(n):
    s = input()
    error = 0

    for j in range(len(s) - 1):  # 문자열 마지막 인덱스 앞에까지 반복문 돌기 (두개씩 비교하기 때문)
        if s[j] != s[j + 1]:  # 두 문자가 다르다면
            new_word = s[j + 1:]  # 뒤 문자 부터 마지막 인덱스까지 새로운 단어 만들기
            if new_word.count(s[j]) > 0:  # 새로만들어진 단어에서 앞의 문자가 존재한다면
                error += 1  # 에러 값에 +1 해주고
                break  # 바로 반복문을 빠져나간다.
    if error == 0:  # 에러가 0이라면 (문자열이 1글자라도 처리가 가능 초기값을 0으로 세팅했기 때문에)
        count += 1  # 그룹단어로 추가

print(count)
