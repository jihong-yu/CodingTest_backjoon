a = int(input())
count = 0
original = a  # 초기 입력값 저장

while True:
    left = a // 10  # 각자리의 숫자를 더하기 위한작업(10의자리)
    right = a % 10  # 각자리의 숫자를 더하기 위한작업(1의자리)
    sum2 = left + right  # 각 자리를 더해준다.

    new = right * 10 + sum2 % 10  # 새로운수 만들기(주어진 수의 오른쪽 자리수(10의자리)와 앞에서 구한 합의 오른쪽자리(1의자리)의 합)
    count += 1  # 연산횟수 1 증가(사이클 길이)
    if original == new: break  # 만약 초기 값과 new의 값이 같다면 반복문을 빠져나온다.
    a = new  # 새로운 수를 a에 대입하여 반복할 수 있게 해준다.

print(count)
