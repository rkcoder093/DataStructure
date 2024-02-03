def printNToOne(start, end):
    if start == 0:
        return
    print(start)
    printNToOne(start-1,end)
    
printNToOne(10,1)
    