#  0 1  1 2 3 5 8 11 19

def recursiveFeb(n):
    if n <= 1:
        return n
    last  = recursiveFeb(n-1)
    alast  = recursiveFeb(n-2)
    return last + alast

print(recursiveFeb(4))
    
    