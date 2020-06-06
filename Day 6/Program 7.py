def Ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return Ackermann(m - 1, 1)
    n2 = Ackermann(m, n - 1)
    return Ackermann(m - 1, n2)

m = int(input("Enter First number"))
n = int(input("Enter Second number"))
print(Ackermann(m, n))
