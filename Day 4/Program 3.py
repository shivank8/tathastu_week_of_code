size = int(input("Enter the size of Dictionary"))
print("Enter the elements for Dictionary")
lst =[]
dic={}
for i in range(size):
    key = input("Enter the key for item in dictonary: ")
    value = int(input("Enter the value for item  in dictonary: "))
    lst.append(value)
lst.sort()
print("The second maximum number is ", lst[1])