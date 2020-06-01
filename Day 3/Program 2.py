str=input("Enter a string:")
for i in range(len(str)+1):
    for j in range(i+1,len(str)+1):
        print(str[i:j])