num=int(input("enter an integer no"))
i=2
count=0
while i <= num :
 if num % i is 0:
    count=count+1
 i=i+1
if count > 1 :
    print("the entered no: is not prime")
else :
    print("the entered no is prime")
