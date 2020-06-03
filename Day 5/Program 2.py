def rep(n):
    lst=list(n)
    for i in range(0,len(lst)):
        lst2=lst[i:]
        lst2.sort()
        lst.pop(i)
        lst.insert(i,lst2[-1])

    for i in lst:
        print(i,end="")

n=input("Enter a number")
rep(n)