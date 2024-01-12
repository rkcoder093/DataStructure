str = 'ritik'
list = []
rev =''
# one by without any built in functions  
for i in str:
    list.append(i)
length = len(list)
for i in range(length-1,-1,-1):
    rev = rev + list[i]
print(rev)

# two  by slicing 
print(str[::-1])

# by join mehtod 
rev_str = ''.join(i for i in reversed(str) )
print(rev_str)

# simple one 
str_value = 'ritik'
reversed_str = ''
for char in str_value:
    reversed_str = char + reversed_str
print(reversed_str)



# solution for this problem as an object.
class reverseStr:
    def __init__(self, input_str):
        self.input_str =input_str   # self inilisized the variables here
    def reverse(self):
        reversed_str = ''
        for char in self.input_str:
            reversed_str = char + reversed_str
        return reversed_str
        
string1 = input('enter your string or word') # input the string 
rev = reverseStr(string1) # createt the object of the class reverseStr 
revers = rev.reverse() # call the function inside the class
print(revers) #print the returned statement
    