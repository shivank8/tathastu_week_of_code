def rep(n):
    lst=list(n)
    for i in range(0,len(lst)):
        if(lst[i]=='0'):
            lst.pop(i)
            lst.insert(i,5)
    for i in lst:
        print(i,end="")
x=(input("Enter a number"))
rep(x)