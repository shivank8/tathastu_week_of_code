size = int(input("enter the size of the list"))
list = []
flag=0
for i in range(size):
   list.append(int(input()))
for i in range(len(list)):
    for j in range(i,len(list)):
        if(list[i]>list[j]):
            flag=1
    for k in range(0,i):
        if (list[i] < list[j]):
            flag = 1
    if(flag==0):
        print("Such a Smallest number is  ",list[i])
        break
if(flag==1):
    print("Sorry no such a number is found")