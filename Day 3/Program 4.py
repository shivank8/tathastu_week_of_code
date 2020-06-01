n=int(input("Enter number of items to add"))
print("Enter the items for list")
list=[]
for i in range(n):
    item=int(input())
    list.append(item)
newList=[]
for i in list:
    if i not in newList:
        newList.append(i)
print(newList)