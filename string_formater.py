def print_formatted(number):
    for i in range(1, number +1):
        octate = ""
        forHex={10:'A', 11:'B', 12:'C',13:'D' , 14:'E' ,15:'F'}
        hexaDecimal = ""
        binary =""
        n = number
        while (n !=0):
            reminder = n % 8
            n = n//8
            octate = str(reminder)+ octate
        n1 = number
        while(n1 > 0):
            reminder = n1% 16
            n1 = n1//16
            if reminder > 9 :
                hexaDecimal  = forHex[reminder] + hexaDecimal
            else:
                hexaDecimal  = str(reminder) + hexaDecimal
        n2 = number 
        while (n2 > 0):
            reminder = n2 % 2
            n2 = n2//2
            binary = str(reminder)+binary
                
        print(octate, hexaDecimal,binary,len(bin(number)[2:]),sep=":")
    
    

if __name__ == '__main__':
    n = 143
    print_formatted(n)