s = input()
croatiaAlphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for j in croatiaAlphabet:
    if j in s:
        s = s.replace(j,"1")

print(len(s))