def creditcard(n):
    orig=n
    digits=[]
    s=0
    while n!=0:
        dig=n%10
        n=n//10
        digits.append(dig)
    digits.reverse()
    for d in digits[-2::-2]:
        if 2*d>9:
            s+=2*d-9
        else:
            s+=d*2
    for d in digits[-1::-2]:
        s+=d
    if s%10==0:
        print('Valid credit card number')
    else:
        print('Invalid credit card number')
    
    
num=int(input('enter credit card number: '))
creditcard(num)

