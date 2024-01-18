def palendrome(number):
    rev_num  = 0
    while (number != 0):
        rev_num = 10 *rev_num + (number % 10 )
        number = number // 10
    return rev_num

number = 1234321
rev = palendrome(number)
if rev == number:
    print('this is same as oposit')
else:
    print('this is not same in opposit')
