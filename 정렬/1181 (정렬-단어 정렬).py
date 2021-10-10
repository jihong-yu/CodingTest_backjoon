n = int(input())  # 문자열로 숫자를 입력받는다.

array = []  # 알파벳를 담을 리스트 선언
setArray = set() #중복을 제거할 set함수 선언
for _ in range(n):
    alphabet = input()
    setArray.add(alphabet)  #중복을 제거하며 set함수에 담는다.

for i in setArray: #set함수의 각 문자열에 접근하여
    array.append(i) #각 문자열을 다시 리스트에 담는다

array.sort()  # 1. 사전순으로 정렬
print(array)
array.sort(key=len)  # 2. 길이대로 정렬
print(array)


for i in array:
    print(i)
