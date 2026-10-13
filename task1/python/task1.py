def triple_and(a,b,c):
    if a==True and b==True and c==True:
        return True
    else:
        return False

print("Enter 0 for 'false' or 1 for 'true' for each of the below:")
a=bool(int(input('a: ')))
b=bool(int(input('b: ')))
c=bool(int(input('c: ')))

print(triple_and(a,b,c))
