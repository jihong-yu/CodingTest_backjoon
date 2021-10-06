n = int(input())

result = 1000001  # 결과값을 초기에 1000001 로 설정(최솟값을 구해야하기 때문)

for i in range(1, n + 1):  # 문제의 범위 1,000,000까지 돈다.

    sumTemp = list(map(int, str(i))) #i가 123 이라면 [1,2,3]으로 리스트에 저장된다.
    sumTemp.append(i)  # 분해하기 전 수 i값을 대입
    sumTemp = sum(sumTemp) #저장되어있는 모든 값들의 합을 대입(생성자구하기)
    
    if sumTemp == n:  # 특정한 수(i)로 계산한 생성자값(sumTemp) 값이 입력한 값(n)과 같다면
        result = min(result, i)  # 특정한 수(i)와 result값을 비교해서 작은 수를 result값에 대입

if result < 1000001:  # 생성자가 있어서 result값이 변경이 되었따면
    print(result)  # 그 값을 출력
else:  # 만약 결과값이 초기설정한 값 그대로라면(생성자가 없다는 뜻)
    print(0)  # 0을 출력
