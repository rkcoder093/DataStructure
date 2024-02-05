n = 6
num =0
for i in range(1, n+1):
    for j in range(1,i):
        num +=1
        print(num, end=" ")
    for k in range((n*2)-1,0, -1):
        print(' ',end=" ")
    print('\n')