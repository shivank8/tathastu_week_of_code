num=input("Enter a number")
num=list(num)
for i in range(len(num)-1,0,-1):
    if num[i]>num[i-1]:
        num3=num[i:]
        num=num[:i]
        num3.sort()
        num.extend(num3)
        num[i],num[i-1]=num[i-1],num[i]
        num="".join(num)
        print(num)
        break
    else:
        continue
else:
    print("Not possible")