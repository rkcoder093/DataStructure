number = 12345678901
rev_num  = 0
while (number != 0):
    rev_num = 10 *rev_num + (number % 10 )
    number = number // 10
    print(rev_num)

