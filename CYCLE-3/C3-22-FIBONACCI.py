def fibonacci(num):
  i=1
  a = -1
  b = 1
  while i <= num :
     c = a + b
     print(c)
     a = b
     b = c
     i = i + 1


n=int(input("enter a limit"))
fibonacci(n)
