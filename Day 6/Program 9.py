size=int(input("enter the size of the list"))
k=int(input("Enter the value of k"))
list=[]
for i in range(size):
    list.append(int(input()))
list.sort()
print(list[k-1])