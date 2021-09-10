input_num = int(input())

line = 0  # 사선 라인
max_num = 0  # 입력된 숫자(input_num 변수)의 라인에서 가장 큰 숫자(1 -> 1, 2-> 2 , 3 -> 4 , 4-> 7 ...)
min_num = 1  # 입력된 숫자(input_num 변수)의 라인에서 가장 작은 숫자(1 -> 1 , 2 -> 3 , 3 -> 6 , 4 -> 10 ...)

while input_num > max_num:  # 조건: 입력한 x번째 수가 해당 라인의 최대값보다 작거나 같다면 빠져 나온다.
    min_num += line  # 각 라인에서의 최솟값
    line += 1  # 해당 input_num이 존재하는 라인 위치
    max_num += line  # 각 라인에서의 최대값

if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = input_num - min_num + 1  # 분자일때는 해당 라인에서 입력합 값에서 최소값을 뺀 수에서 + 1
    under = max_num - input_num + 1  # 분모일때는 해당 라인에서 최대값에서 입력한 값을 뺀 수에서 + 1
else:  # 사선 라인이 홀수번째 일 때
    top = max_num - input_num + 1  # 분자일때는 해당 라인에서 최대값에서 입력한 값을 뺀 수에서 + 1
    under = input_num - min_num + 1  # 분모일때는 해당 라인에서 입력합 값에서 최소값을 뺀 수에서 + 1

# print(f'{top}/{under}') #f스트링을 이용한 출력방법
print(top, under, sep="/") #sep 인자를 이용한 출력방법
