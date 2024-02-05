class fib:
    def __init__(self ,num ):
        self.num = num 
    def seriesUpToTheDigit(self, number =None):
        if number is None:
            number = self.num
        
        num1 = [0,1]
        
        for i in range(1, number-1):
            num1.append(num1[-1] + num1[-2])
        return num1
            
    def seriesUpToTheNumber(self, number =None):
        if number is None:
            number = self.num
        
        num2 = [0,1]
        while (num2[-1] +num2[-1] <=number):
            num2.append(num2[-1]+num2[-2])
        return num2
        
        
numb = int(input('enter a number'))
f = fib(numb)
print(f.seriesUpToTheDigit())
print(f.seriesUpToTheNumber())

            
            
                
        
