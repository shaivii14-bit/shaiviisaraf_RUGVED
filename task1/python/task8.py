def sequence(n,s):
    if len(s)%n!=0 or n>len(s) or n<=0:
       print("Division is not possible because of unsuitable value of n!")
    substr=s[:len(s)//n]
    if s!= n*substr:
        print("Division is not possible because sequences are not equal!")
    else:
        for i in range(n):
            print(substr, end=', ')
        
    
num=int(input('enter n: '))
string=input('enter string:')
sequence(num, string)

