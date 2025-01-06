import math

class Shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius =radius
    def calculate_area(self):
        return math.pi *self.radius**2
    def calculate_perimeter(self):
        return 2*math.pi*self.radius
    

class Trinagle(Shape):
    def __init__(self,base,height,side1,side2,side3):
        self.base =base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculate_area(self):
        return 0.5*self.base*self.height
    
    def calculate_perimeter(self):
        return self.side1+self.side2+self.side3
    

class Square(Shape):
    def __init__(self,length):
        self.lenght = length
    
    def calculate_area(self):
        return self.lenght ** 2
    
    def calculate_perimeter(self):
        return 4*self.lenght
    
#object for Square
squareObj = Square(5)
print("Area of Square:",squareObj.calculate_area())
print("Perimeter of Square:",squareObj.calculate_perimeter())

#object for Triangle
triangleObj = Trinagle(5,10,3,4,5)
print("Area of Triangle:",triangleObj.calculate_area())
print("Perimeter of Triangle:",triangleObj.calculate_perimeter())

#object for Triangle
cicleObj = Circle(10)
print("Area of Circle:",triangleObj.calculate_area())
print("Perimeter of Circle:",triangleObj.calculate_perimeter())
