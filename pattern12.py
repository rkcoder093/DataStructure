n = 5
for i in range(1, n+1):
    for j in range(1,i):
        print(j, end=" ")
    for k in range((n*2)-1,0, -1):
        print(' ',end=" ")
    for l in range(i-1,0,-1):
        print(l, end=" ")
    n = n-1
    print('\n')
