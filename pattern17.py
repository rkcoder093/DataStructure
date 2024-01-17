n = 5
for i in range(1,n+1):
    n = n-1
    for j in range(1,n+1):
        print(' ', end=" ")
    for k in range(1,(i+1)):
        print(chr(64+k),end=" ")
    for k in range(i-1 , 0 , -1):
        print(chr(64+k),end=" ")

    print('\n')
