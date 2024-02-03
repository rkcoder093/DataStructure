def pattern(num1 , num2):
    range1 = int ((num1-1)/2)
    r = range1
    r = int((num1-1)/2)
    for i in range(1,range1+1):
        for j in range(1, 3*(r) +1):
            print("-" , end="")
        for k in range(1, (i*2)):
            print(".|.", end="")
        for j in range(1, 3*(r) +1):
            print("-" , end="")
        r = r-1
        print()
    print("WELCOME".center(num2,'-'))
    r = num1 -2
    for i in range(1, range1+1):
        for j in range(1, i*3+1):
            print('-' , end="")
        for k in range(1,r+1):
            print(".|.", end="")
        for j in range(1, 3*(i) +1):
            print("-" , end="")
        r = r-2
        print()
# number1 is x then number2 is 3x
str = input()
s = str.split(' ')
number1 = int(s[0])
number2 = int(s[-1])
pattern(number1, number2)
