def pyramid(n):
    for i in range(0,n+1):
        print("\r") 
        for j in range(1,i+1):
            print(i*j,end=" ")
        
num=int(input("enter the limit"))  
pyramid(num)        