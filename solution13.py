def printNTinesName(i, n):
    if i>n:
        return
    print('ritik', i, sep=':')
    printNTinesName(i+1,n)
    
printNTinesName(1,100)