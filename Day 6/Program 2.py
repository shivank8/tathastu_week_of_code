size=int(input("enter the size of the list"))
list=[]
flag=0
for i in range(size):
    item=int(input())
    list.append(item)
    if(item!=1 and item!=0):
        flag=1
        break
list.sort(reverse=True)
if(flag==0):
    print("Sorted list is ")
    print(list)
else:
    print("Sorry ,the given also contains element other than 0 and 1. Please try again. ")