class Calculator:
    def __init__ (self, num):
        self.num = num

    def __add__(self, other):
        return Calculator(self.num + other.num)

    def __sub__(self, other):
        return Calculator(self.num - other.num)

    def __mul__(self, other):
        return Calculator(self.num * other.num)

    def __truediv__(self, other):
        return Calculator(self.num / other.num) 
        
    def __str__(self):
        return str(self.num)

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")