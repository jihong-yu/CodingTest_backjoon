N = int(input())


def max_(score):
    max_ = 0
    for i in score:
        if i > max_:
            max_ = i
    return max_


def sum_(score):
    sum_ = 0
    for i in score:
        sum_ += i
    return sum_


score = list(map(int, input().split()))
M = max_(score)
for i in range(len(score)):
    score[i] = score[i] / M * 100
print(sum_(score) / N)
