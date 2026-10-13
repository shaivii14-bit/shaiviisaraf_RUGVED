def ColemanLiau(s):
    totalsentences=s.count('. ')+s.count('?')+s.count('!')
    totalwords=len(s.split())
    totalchar=0
    for char in s:
        if char.isalnum():
            totalchar+=1

    print(totalsentences, totalwords, totalchar)
    L=(totalchar/totalwords)*100
    S=(totalsentences/totalwords)*100
    CLI=0.0588*L -0.296*S -15.8
    print('Grade level= ',CLI)
    
    
string=input('enter text: ')
ColemanLiau(string)

