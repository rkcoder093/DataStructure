n=3
for i in range(0,(2*n-1)):
    for j in range(0 , (2*n-1)):
        top = i
        left = j
        bottom = 2*n -2  -j     
        down = 2*n -2 -i
        print(n-min(top,left,bottom,down),end=' ')
    print('\n')
