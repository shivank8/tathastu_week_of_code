n = int(input("Enter size of array"))
arr = []
flag=0
for i in range(n):
    arr.append(int(input()))
for i in range(n-1):
    if(arr[i]<arr[i+1]):
        flag=1
        break
if flag==0:
    print("Yes, the list is sorted and rotated")
else:
    print("No, the list is not sorted and rotated")
