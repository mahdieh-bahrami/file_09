class Rectangle:
    def __init__(self, length, Width):
        self.l = length
        self.w = Width
    def Area(self):
        return self.l * self.w
    def Perimeter(self):
        return (self.l + self.w) * 2
    def Comparison(self, other):
        a1 = self.l * self.w
        a2 = other.l * other.w
        if(a1 > a2):
            return True
        else:
            return False
obj1 = Rectangle(4,2)
print('\nRectangle 1')
print(f'Area       : {obj1.Area()}')
print(f'Perimeter  : {obj1.Perimeter()}')
# 
obj2 = Rectangle(2,2)
print('\nRectangle 2')
print(f'Area       : {obj2.Area()}')
print(f'Perimeter  : {obj2.Perimeter()}')
# 
c = obj1.Comparison(obj2)
if(c):
    print(f'\nComparison : True')
else:
    print(f'\nComparison : Flase')