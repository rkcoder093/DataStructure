n=10
for i in range(1,n):
    if i == 1 or i == n-1:
        for j in range(1,n):
            print('*', end=" ")
    else:
        for j in range(1 , n):
            if j ==1 or j == n-1:
                print('*',end=" ")
            else:
                print(' ', end=' ')
            
    print('\n')