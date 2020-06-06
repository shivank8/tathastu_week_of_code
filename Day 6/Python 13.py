size = int(input("enter the size of the Array"))
arr = []
flag=0
for i in range(size):
    arr.append(int(input()))
arr.sort()
for i in range(len(arr)-2):
    a=arr[i]
    b=arr[i+1]
    c=arr[i+2]
    if(a+b+c<2 and a+b+c>1):
        flag=1
        break
if(flag==1):
    print("The triplet available is" , a,b,c)
else:
    print("No such a triplet is found.")