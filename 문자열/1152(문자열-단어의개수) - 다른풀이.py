S = input()

# 문자열이 공백 하나만 있을 경우
if S.count(" ") == len(S):
    print(S.count(" ") - 1)
    exit()

# 문자열의 첫번째가 공백일 경우
if S[0] == ' ':
    S = S[1:]

# 문자열의 끝이 공백일 경우
if S[len(S) - 1] == ' ':
    S = S[:-1]

# 공백의 개수에서 + 1 해준다.
print(S.count(" ") + 1)
