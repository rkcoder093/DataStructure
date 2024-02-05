def printNumber(end , start=1 ):
    if end < start:
        return
    print(start)
    printNumber(start=start+1, end=end)   
printNumber(end=10)
