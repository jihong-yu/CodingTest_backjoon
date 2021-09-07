words = input().upper()  # 입력을 대문자로 받는다.

unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []  # 반복횟수를 담기 위한 리스트 초기화

for x in unique_words:  # 입력받은 문자 열에서 중복을 제거한 각각의 문자들을 사용
    cnt = words.count(x)  # 해당 단어들이 개수가 몇개있는지 체크
    cnt_list.append(cnt)  # 개수를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1:  # 개수의 최대값이 중복되면
    print('?')  # ?를 출력

else:  # 그렇지 않을 경우
    max_index = cnt_list.index(max(cnt_list))  # count 숫자(개수의) 최대값 인덱스(위치) 를 찾는다.
    print(unique_words[max_index])  # 해당 인덱스에 있는 단어 출력
