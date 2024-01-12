
class stringOperations:
    def __init__(self, stri):
        self.stri = stri
    def palendrome(self):
        rev = self.stri[::-1]
        print(rev, self.stri, sep=" ")
        if self.stri == rev:
            
            return True
        else:
            return False
    
name = 'abcba' 
n = stringOperations(name)

print(n.palendrome())