croatia = ["c=", "c-", "dz=", "z=", "d-", "lj", "nj", "s="]

word = input()
count = 0
word_len = len(word)

for i in croatia:  # 크로아티아 문자가 저장된 리스트를 돈다.
    if i in word:  # 만약 크로아티아 문자가 입력받은 단어에 있다면
        count += word.count(i)  # 그 개수를 count값에 저장
        word_len -= (word.count(i) * len(i))  # 그 단어의 길이 * 개수 만큼 단어의 길이에서 제외시킨다.
        word = word.replace(i, " ")  # 또한 그 단어를 공백으로 치환한다.

print(word_len + count)  # 크로아티아를 제외한 단어의 길이와 크로아티아 단어의 개수를 더해준다.
