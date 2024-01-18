def armstrong_number(number):
    numb_list = []
    num = number
    armstrong_numbers = 0
    while (num != 0):
        numb_list.append(num%10)
        num = num //10 
    for i in numb_list:
        armstrong_numbers += i**(len(numb_list))
    if armstrong_numbers == number:
        return True
    else:
        return False
    
arms_number = armstrong_number(1634)
print(arms_number)
