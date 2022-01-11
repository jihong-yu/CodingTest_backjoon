num = input()  # 문자열 num을 입력받는다.

if int(num) < 10:  # 만약 num이 10보다 작다면
    num = "0" + num  # num의 값 앞에 0을 붙여 준다.

original = num  # num의 값의 초기 값을 저장한다.

sum = 0  # 합을 저장하기 위한 sum값 정의
count = 0  # 횟수를 세기 위한 count 값 정의

while True:  # 무한번 돈다.

    sum = int(num[0]) + int(num[1])  # 숫자의 앞자리와 뒷자리를 더한다.

    if len(str(sum)) == 1:  # 만약 길이가 1이라면
        new_num = num[1] + str(sum)[0]  # 기존의 숫자의 뒷자리와 합계의 한자리를 더한다.
    else:
        new_num = num[1] + str(sum)[1]  # 기존의 숫자의 뒷자리와 합계의 뒷자리를 더한다.

    num = new_num  # 새로 나온 수를 기존의 num에 대입해준다.(계속해서 값을 계산하기 위해)
    count += 1  # 횟수를 1 증가한다.

    if num == original:  # 만약 초기 값과 변화된 num 값이 다시 동일해 졌다면
        print(count)  # 횟수를 출력후
        break  # 반복문을 빠져 나온다.
