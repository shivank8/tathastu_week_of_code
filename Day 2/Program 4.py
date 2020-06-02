a=5
b=5
count=0
for i in range(0,10):
    count+=1
    for j in range(0,11):
        if(j>=a and j<=b):
            print(" ",end="")
        else:
         print("*",end="")
    print(" ")
    #print(count)
    if(count<5):
        a-=1
        b+=1
    elif(count==5):
         j=5
    else:
        a+=1
        b-=1
