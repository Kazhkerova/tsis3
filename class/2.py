class Shape:
    def area(self):
        return 0
class Square(Shape) :  
    def __init__(self,l):
        self.l=l

    def area(self):
        return self.l * self.l


l_shape=float(input())
shape=Shape()
print(shape.area())
l_square=float(input())
square=Square(l_square)
print(square.area())