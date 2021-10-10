import sys
from collections import Counter

n = int(input())  # 문자열로 숫자를 입력받는다.

array = list(map(int, input().split()))

array2 = sorted(set(array))  # array를 set형으로 바꿔 중복을 제거한 후 다시 정렬하여 리스트로 반환

array3 = {array2[i]: i for i in range(len(array2))} #dictionary자료형을 이용해야한다.(key,value 형태로저장이됨)

for i in array:
    print(array3[i], end=" ")
    # dict형은 순서가없는 hashmap형태이기 때문에 array3['찾고자하는 자료형']을 하면 해당하는 value 값을 리턴

print(*[array3[i] for i in array]) #다음과 같이 출력이 가능 여기서 * 는 컨테이너타입(리스트,셋 등등)의 내부를 unpacking할때 사용된다.