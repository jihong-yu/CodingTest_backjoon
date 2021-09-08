s = input()
temp = 0
for i in range(s.__len__()):
    if s[i] == "A" or s[i] == "B" or s[i] == "C":
        temp += 3
    elif s[i] == "D" or s[i] == "E" or s[i] == "F":
        temp += 4
    elif s[i] == "G" or s[i] == "H" or s[i] == "I":
        temp += 5
    elif s[i] == "J" or s[i] == "K" or s[i] == "L":
        temp += 6
    elif s[i] == "M" or s[i] == "N" or s[i] == "O":
        temp += 7
    elif s[i] == "P" or s[i] == "Q" or s[i] == "R" or s[i] == "S":
        temp += 8
    elif s[i] == "T" or s[i] == "U" or s[i] == "V":
        temp += 9
    elif s[i] == "W" or s[i] == "X" or s[i] == "Y" or s[i] == "Z":
        temp += 10

print(temp)
