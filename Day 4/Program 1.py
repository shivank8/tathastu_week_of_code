size = int(input("Enter the size of tuple"))
print("Enter the elements for tuple")
lst =[]
for i in range(size):
    lst.append(int(input()))
tpl=tuple(lst)
n=int(input("Enter a item to find occurance"))
count=0
for i in tpl:
    if(i==n):
      count+=1
print("Occurance of the given item is",count)