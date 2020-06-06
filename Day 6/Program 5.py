n = int(input("Enter size of array"))
arr = []
sum = 0
c = 0
for i in range(n):
    item = int(input())
    arr.append(item)
    sum += item
while c >= sum:
    a = arr[:-2]
    b = arr[:-1]
    c = a+b
    arr.append(c)
    a = b
    b = c
if sum in arr:
    print("Yes,the sum is also a fibonacci number")
else:
    print("No,the sum is not a fibonacci number")