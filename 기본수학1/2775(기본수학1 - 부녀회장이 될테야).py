t = int(input())  # 전체 테스트케이스 수

for _ in range(t):
    k = int(input())  # 층의 개수
    n = int(input())  # 호의 개수
    array2 = [[] for i in range(k + 1)]  # 각 층마다 + 각 층의 각 호마다 사람수를 입력하기 위한 이중리스트 선언
    array2[0] = [i for i in range(1, 14)]  # 0층의 각 호의 사람은 1~14 명으로 지정
    for i in range(1, k + 1):  # 입력한 층의 개수 까지 돈다
        for j in range(n):  # 입력한 호의 개수까지 돈다
            array2[i].append(sum(array2[i - 1][0:j + 1]))  # 각층의 각 호마다 이전층의 같은 호까지의 사람수를 더한다

    print(array2[k][n - 1])  # 해당 층과 호의 사람수를 출력 단, n은 위의 반복문에서 0부터 시작했기 때문에 n-1로 인덱스를 맞춰준다.
