from src.calculator.operators.addition import addition
from src.calculator.operators.subtraction import subtraction
from src.calculator.operators.multiplication import multiplication
from src.calculator.operators.division import division
from src.calculator.operators.square import square
from src.calculator.operators.square_root import square_root

class Calculator:
    result = 0

    def __init__(self):
        pass

    @staticmethod
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result
    
    @staticmethod
    def sub(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    @staticmethod
    def mult(self, a, b):
        self.result = multiplication(a, b)
        return self.result
    
    @staticmethod
    def divi(self, a, b):
        self.result = division(a, b)
        return self.result
    
    @staticmethod
    def squ(self, a):
        self.result = square(a)
        return self.result
    
    @staticmethod
    def root(self, a):
        self.result = square_root(a)
        return self.result
