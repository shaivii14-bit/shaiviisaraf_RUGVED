def sort(s):
    charlist=[]
    count={}
    for char in s:
        charlist.append(char)
        count[char]=charlist.count(char)
    charlist.sort()

    s=""
    for char in charlist:
        count[char]=charlist.count(char)
        s+=char
    print('Count for every character in string:', count)   
    print('Sorted string:\n', s)
    

s=input('enter string to be sorted: ')

sort(s)
