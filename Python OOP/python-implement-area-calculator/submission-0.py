import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length: int, width: int =0):
        if width:
            area_val = length * width
            return area_val
        else:
            area_val = math.pi * (length ** 2)
            return round(area_val, 2)
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
