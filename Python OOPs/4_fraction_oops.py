class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        
        temp_num = self.num * other.den + self.den * other.num
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num, temp_den)


    def __sub__(self, other):
        
        temp_num = self.num * other.den - self.den * other.num
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num, temp_den)

    
    def __mul__(self, other):
        
        temp_num = self.num * other.num
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num, temp_den)

    
    def __truediv__(self, other):
        
        temp_num = self.num * other.den
        temp_den = self.den * other.num

        return "{}/{}".format(temp_num, temp_den)


x = Fraction(3,4)

print(type(x))

print(x)

y = Fraction(5,6)
print(y)

print("Fraction addition is : ", x + y)
print("Fraction subtraction is : ", x - y)
print("Fraction multiplication is : ", x * y)
print("Fraction division is : ", x / y)

# Instance Variable:- Instance varibale are variable for which value of 
# variable is different for different object.
