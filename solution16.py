def PrintNNumber(num):
    if num == 0:
        return 0
    return num + PrintNNumber(num-1)
    
print(PrintNNumber(10))


def recursivePrint(i,sum):
    if i<1:
        print(sum)
        return
    recursivePrint(i-1,sum+i)

recursivePrint(10,0)