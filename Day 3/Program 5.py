n1=int(input("Enter number of items to add in list 1"))
n2=int(input("Enter number of items to add in list 2"))
list1=[]
list2=[]
print("Enter items for list 1")
for i in range(n1):
    item=int(input())
    list1.append(item)
print("Enter items for list 2")
for j in range(n2):
    item=int(input())
    list2.append(item)
print("Intersection of given two lists is")
for i in list1:
    for j in list2:
        if(i==j):
            print(i)