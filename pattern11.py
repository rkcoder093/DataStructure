num = 1
for i in range(1,6):
    for j in range(1, i+1):
        print(num, end=" ")
        if num ==0 : num = 1
        else: num = 0
    print('\n')
