def lettercount(word):
    letters={}
    for l in word:
        letters[l]=word.count(l)
    return letters
    
w1=input('enter word 1: ')
w2=input('enter word 2: ')
if lettercount(w1)==lettercount(w2):
    print(w1,'and',w2,'are anagrams')
else:
    print(w1,'and',w2,'are not anagrams')
    

