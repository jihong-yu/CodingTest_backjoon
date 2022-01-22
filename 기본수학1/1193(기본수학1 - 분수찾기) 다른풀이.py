x = int(input())
n = 1
k = 1

while True:

    # 등차수열의 범위를 k로 설정
    # 1,3,6,10,15 ...
    # n = 1 일때는 1 , n = 2일때는 2,3 , n = 3 일때는 4,5,6 , n = 4 일때는 7,8,9,10 ...
    range_ = k

    # 만약 입력받은 숫자가 해당 범위안에 있다면
    if x <= range_:
        # i번째 등차수열에서 시작값을 설정(1,2,4,7,11 ....)
        start = k - n + 1

        # 만약 입력받은 수가 짝수번째 패턴에 존재한다면
        if n % 2 == 0:
            top = 1  # 분자를 1로 설정
            bottom = n  # 분모를 n으로 설정

            while True:
                # 만약 start값이 입력받은 횟수와 같아 졌다면
                if start == x:
                    print(f"{top}/{bottom}")
                    exit()

                top += 1  # 분자를 +1씩 해준다
                bottom -= 1  # 분모를 -1씩 해준다.
                start += 1  # 입력받은 횟수에 가기위해 start값을 1씩 증가한다.

        # 만약 입력받은 수가 홀수번째 패턴에 존재한다면
        else:
            top = n  # 분자를 n으로 설정
            bottom = 1  # 분모를 1로 설정

            while True:
                # 만약 start값이 입력받은 횟수와 같아 졌다면
                if start == x:
                    print(f"{top}/{bottom}")
                    exit()

                top -= 1  # 분자를 -1씩 해준다
                bottom += 1  # 분모를 +1씩 해준다.
                start += 1  # 입력받은 횟수에 가기위해 start값을 1씩 증가한다.

    # 등차수열로 증가하기때문에 (1,3,6,10) n의 값을 1씩 증가
    n += 1
    # 등차수열을 표현하기 위해 증가한 n의 값을 그대로 k에 더해준다.
    k += n
