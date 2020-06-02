n=int(input("Enter a number"))
if(n%2==0):
    print("Number is Even")
else:
    print("Number is Odd")
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count==2):
    print("NUmber id Prime")
else:
    print("Number is not Prime")
copy=n
new=0
while(copy>0) :
    digit=copy%10
    new=new*10 +digit
    copy=int(copy/10)
if(new==n):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
copy=n
sum=0
while(copy>0):
    digit=copy%10
    sum=sum+digit*digit*digit
    copy=int(copy/10)
if(sum==n):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")