def fibonacci(n):
    if n==1:
        print(0)
    elif n==2:
        print(1)
    else:
        n1=0
        n2=1
        print(n1)
        print(n2)
        for i in range(n-2):
            n3=n1+n2
            print(n3)
            n1=n2
            n2=n3
    
    
num=int(input('enter n: '))
fibonacci(num)