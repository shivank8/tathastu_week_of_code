size=int(input("Enter the size of the Dictionary"))
disc=[]
print("Enter items of Dictionary")
for i in range(size):
    disc.append(input())
sizeList = int(input("Enter the size of the List"))
print("Enter items of List")
lst=[]
for i in range(sizeList):
    lst.append(input())
for i in disc:
    flag=0
    for j in i:
        if j not in lst:
            flag=1
    if(flag==0):
        print(i, end=" ")
