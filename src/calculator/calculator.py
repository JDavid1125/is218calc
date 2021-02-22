from src.calculator.addition import addition
from src.calculator.subtraction import subtraction
from src.calculator.multiplication import multiplication
from src.calculator.division import division
from src.calculator.square import square


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def sub(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def mult(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divi(self, a, b):
        self.result = division(a, b)
        return self.result

    def squ(self, a):
        self.result = square(a)
        return self.result