def prefix(s1, s2):
    if (s1 < s2):
        m = len(s1)
    else:
        m = len(s2)
    s = ""
    for i in range(m):
        if (s1[i] == s2[i]):
            s = s + s1[i]
        else:
            break
    print("Longest common prefix is ",s)


s1 = input("Enter first String")
s2 = input("Enter second String")
prefix(s1,s2)

