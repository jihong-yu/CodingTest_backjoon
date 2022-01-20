def solution(word):
    for i in set(word):  # set을 이용하여 단어의 중복을 없앤 채 돈다.
        if word.count(i) >= 2:  # 만약 단어의 길이가 2이상인 문자열이 있다면
            list_ = []  # 해당 문자의 인덱스를 담을 리스트 선언
            start = -1  # 시작값 -1로 설정
            while True:  # 반복문을 돈다
                start += 1  # 시작값에 + 1
                start = word.find(i, start)  # 단어의 인덱스를 start를 기점으로 찾는다.
                if start == -1:  # 만약 해당 단어가 더이상 없다면
                    break  # 탈출
                list_.append(start)  # 리스트에 해당 인덱스 값을 추가한다.
            for j in range(len(list_) - 1):  # 저장된 인덱스의 길이 만큼 반복문을 돈다.
                if list_[j + 1] - list_[j] > 1:  # 만약 저장된 인덱스의 차가 1보다 크다면(즉, 그룹단어가 아니라면)
                    return 0  # 0을 반환

    return 1  # 만약 위의 조건에 걸리지 않는다면 그룹단어 이므로 1을 반환


T = int(input())
count = 0

for _ in range(T):
    word = input()
    count += solution(word)

print(count)
