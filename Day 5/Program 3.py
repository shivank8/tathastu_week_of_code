def thief(house,first):
    stolenValue=0
    for i in range(first,len(house),2):
        stolenValue+=house[i]
    return stolenValue
n=int(input("Enter the number of houses"))
print("Enter the values sored in these houses")
house=[]
for i in range(n):
    house.append(int(input()))
if(thief(house,0)>thief(house,1)):
    print("The maximum stolen value from Houses is",thief(house,0))
else:
    print("The maximum stolen value from Houses is",thief(house,1))