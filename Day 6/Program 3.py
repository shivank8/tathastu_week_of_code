size=int(input("enter the size of the list"))
list=[]
flag=0
for i in range(size):
    list.append(int(input()))
list.sort()
for i in range(len(list)):
    if(i!=list[i]):
        flag=1
        break
if(flag==0):
    print("Smallest number missing from the list is",list[i]+1)
else:
    print("Smallest number missing from the list is",i)