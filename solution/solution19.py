def revString(str,start):
    if start >= len(str) / 2:
        return True
    if str[start] != str[len(str)-start-1] :
        return False
    return revString(str, start+1) 

print(revString('ABCBA',start= 0))

str1 = 'ritik'
# lisst = list(str1)
# print(len(str1))