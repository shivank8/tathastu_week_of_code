x=int(input("Enter number of items to add"))
print("Enter the items for list")
list=[]
n=1
for i in range(x):
    item=int(input())
    list.append(item)
list.sort()
newlist=[]
sum=0
for i in range(len(list)):
    newlist.append(list[i])
    sum=list[i]
    for j in range(i+1,len(list)):
        sum=sum+list[j]
        newlist.append(sum)
newlist=set(newlist)
print(newlist)
