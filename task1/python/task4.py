def selectionsort(s):
    charlist=[]
    for char in s:
        charlist.append(char)

    for i in range(0,len(charlist)-1):    #passes
        minindex=i
        for j in range(i+1,len(charlist)):
            if charlist[j]<charlist[minindex]:
                minindex=j
        charlist[i],charlist[minindex]=charlist[minindex],charlist[i]
    s=''.join(charlist)
    print(s)
   
    
string=input('enter string: ')
selectionsort(string)

