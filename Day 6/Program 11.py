size=int(input("enter the size of the list"))
list=[]
for i in range(size):
    list.append(int(input()))
list.sort()
product=list[-1]*list[-2]*list[-3]
print(product)