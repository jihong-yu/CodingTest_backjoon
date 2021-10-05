def reflexive(a: int) -> int:
    if a > 0:
        return a * reflexive(a - 1)
    else:
        return 1


n = int(input())
print(reflexive(n))
