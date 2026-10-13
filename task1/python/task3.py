def hill(n):
    orig=n
    digits=[]
    while n!=0:
        dig=n%10
        n=n//10
        digits.append(dig)

    maxindex=digits.index(max(digits))
    if maxindex==0 or maxindex==len(digits)-1:
        return False
    for i in range(0,maxindex):
        if digits[i]>=digits[i+1]:
            return False
    
    for i in range(maxindex,len(digits)-1):
        if digits[i]<=digits[i+1]:
            return False

    return True
    
    
    

num=int(input('enter number: '))

if hill(num):
    print(num,'is a hill number')
else:
    print(num,'is not a hill number')

'''
hill number not if
each digit increasing
each digit decreasing
each digit equal

hill number if
dig0<dig1<....<dign-1>dign
'''
