k=int(input("Enter the value of k"))
mainList=[]
for i in range(k):
    size = int(input("enter the size of the list"))
    list = []
    for i in range(size):
        list.append(int(input()))
    mainList.extend(list)
print(mainList)