number  = 33
factors =[]
for i in range(1, number+1):
    if number % i ==0 :
        factors.append(i)
print(factors)
def prime(n):
    for i in range(2,n):
        if n % i ==0:
            return False
    return True
if number == 1 or number ==0:
    print('this is not considerable')
elif len(factors) ==2:
    print('this is prime')
else: 
    print('this is not prime')
print(prime(33))