n = input()

alphabet = list(range(97,123)) # == list(range(ord("a"),ord("z")+1)

for x in alphabet:
    print(n.find(chr(x)),end=" ") #문자열 내부에  (chr(x))의 값이 있으면 해당문자열의 첫번째 위치를 반환 없으면 -1 반환




