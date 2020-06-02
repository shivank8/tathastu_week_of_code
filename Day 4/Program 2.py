size = int(input("Enter the size of tuple"))
print("Enter the elements for tuple")
lst =[]
for i in range(size):
    lst.append(int(input()))
lst.sort()
print("Tuple after being sort")
print(tuple(lst))