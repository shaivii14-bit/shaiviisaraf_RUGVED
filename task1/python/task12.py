def pattern(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ',end='')
        print('* '*i)
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ',end='')
        print('* '*i)
    
    
num=int(input('enter number: '))
pattern(num)

