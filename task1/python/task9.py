def encrypt(key,s):
    news=''
    for char in s:
        news+=chr(ord(char)+key)
    return news
    
    
k=int(input('enter key: '))
string=input('enter string:')
print(encrypt(k, string))

