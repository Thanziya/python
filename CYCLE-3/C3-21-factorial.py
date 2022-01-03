def factorial(f):
    i=1
    fact=1
    while i<=f:
        fact=fact*i
        i=i+1
    print(fact)

f=int(input("enter an integer"))
factorial(f)
