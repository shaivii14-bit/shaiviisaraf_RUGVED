def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        fibo=fibonacci(n-1)+fibonacci(n-2)
        return fibo
    
    
num=int(input('enter n: '))
print('fibonacci number ',num,'= ', fibonacci(num))
