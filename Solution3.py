class Operations:
    def __init__(self, num):
        self.num = num
    def findFactorial(self, number=None):
        if number is None:
            number = self.num
        if number <0:
            return 'we cant not find the factorial of negative number'
        elif number == 1 or number == 0:
            return number
        else:
            factorial = number * self.findFactorial(number -1)
            return factorial

number = int(input('enter an number')) 
f = Operations(number)
find = f.findFactorial()
print(f'factorial of {number} is : {find}')



fuck = 1 
for i in range(1, number+1):
    fuck = fuck *i
print(fuck  )
