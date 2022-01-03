
def factors(n):
  i=1
  print("factors are")
  while i<=n :
     if (n % i)== 0:
         print(i)
     i=i+1
num=int(input("enter an integer"))
factors(num)
