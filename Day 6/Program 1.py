s=input("Enter a string")
l=list(s)
l.sort()
c=0
for i in l:
    count=0
    for j in l:
        if i==j:
            count+=1
    if count==1:
        l.remove(i)
        c+=1
print("The minimum number of letters to be removed is ",c+1)
