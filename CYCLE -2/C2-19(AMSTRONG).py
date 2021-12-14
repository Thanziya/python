num1=int(input("enter a positive integer"))
s=0
temp=num1
while(temp>0):
    t=temp%10
    s=s+(t**3)
    temp//=10

if s == num1:
    print("armstrong!!")
else:
    print("not an armstrong")
