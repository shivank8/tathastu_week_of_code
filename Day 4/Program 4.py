size = int(input("Enter the size of Dictionary"))
lst =[]
print("Enter the value for item in dictionary")
for i in range(size):
    lst.append(int(input()))
for i in lst:
    count=0
    for j in lst:
        if(i==j):
            count+=1
    if(count>1):
        lst.remove(i)
print(lst)