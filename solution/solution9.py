def HCF(num1, num2):
    if num1 > num2:
        (num1 , num2) = (num2 , num1)
    # min_number_list =[]
    # max_number_list =[]
    common_factors=[]
    for i in range(1,num2+1):
        if num1 % i == 0 :
            if num2 %i == 0:
                common_factors.append(i)
    # for i in min_number_list:
    #     for j in max_number_list:
    #         if i == j :
    #             common_factors.append(i)
    print(f'numer1 is: {num1} factors are and  number 2 is: {num2} factors are  and common factors is {common_factors} and HCF is {common_factors[-1]}')


HCF(45,10)        