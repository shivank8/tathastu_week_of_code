def sorting(lst,size):
    evenlist=[]
    for i in range(size-1):
        if(lst[i]%2==0):
            evenlist.append(lst[i])
            lst.pop(i)
            size-=1
    lst.sort()
    evenlist.sort()
    evenlist.reverse()
    #lst.Extend(evenlist)
    print("The final list after sorting is")
    print(lst)
    print(evenlist)
size=int(input("Enter the size of the list"))
print("Enter the items of list")
lst=[]
for i in range(size):
    lst.append(int(input()))
sorting(lst,size)
