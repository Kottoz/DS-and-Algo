"""
Author: Mohamed Tarek Mohamed
E-mail: mohamedtareck95@gmail.com
"""

"""
Project Name: Length
Description: 
    We will demonstrate the Length class and how you can overload the "+" operator for your own class. 
    To do this, we have to overload the __add__ method. 
    Our class contains the __str__ and __repr__ methods as well.
    The instances of the class Length contain length or distance information. 
    The attributes of an instance are self.value and self.unit.

This class allows us to calculate expressions with mixed units like this one:
>>> 2.56 m + 3 yd + 7.8 in + 7.03 cm

The class can be used like this:

from unit_conversions import Length
L = Length
print(L(2.56,"m") + L(3,"yd") + L(7.8,"in") + L(7.03,"cm"))

>>> 5.57162
"""
class Length:

    __metric =  {'mm' : 0.001, 'cm' : 0.01, 'm' : 1, 'km' : 1000,
                 'inch' : 0.0254, 'feet' : 0.3048, 'yard' : 0.9144,
                 'mi' : 1609.344  }

    def __init__(self, value, unit = 'm'):
        self.value = value
        self.unit = unit 
    
    def converse_to_meter(self):
        return self.value * Length.__metric[self.unit]
    
    def __str__(self):
        return str(self.converse_to_meter())

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            l = self.converse_to_meter() + other
        else:
            l = self.converse_to_meter() + other.converse_to_meter()
        return Length(l / Length.__metric[self.unit], self.unit )

    def __iadd__(self, other):
        if type(other) == int or type(other) == float:
            l = self.converse_to_meter() + other
        else:
            l = self.converse_to_meter() + other.converse_to_meter()
        self.value = l / Length.__metric[self.unit]
        return self

if __name__ == "__main__":

    x = Length(3, "yard") + 5
    print(x)
    
