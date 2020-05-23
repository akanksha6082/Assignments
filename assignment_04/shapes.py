import math
from abc import ABC, abstractmethod
class shapes:
    pi = math.pi

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Triangle(shapes):

        def __init__(self):
            self.sides = 3
        
        def description(self):
            print("All the triangles have three sides and three angles")
        
class Rightangled(Triangle):

        def side_length(self, base, heigth, hypo):
            self.base = base  
            self.heigth = heigth  
            self.hypo = hypo
        
        def area(self):
            print(0.5 * self.base * self.heigth)
        
        def perimeter(self):
            print(self.base + self.heigth + self.hypo)
        
        def description(self):
            print("Right angled triangle has 3 edges and one of the three angle is 90")
        

class IsocelesrightAngled(Rightangled):

        def description(self):
                Rightangled.description(self)
                print("but isoceles triangle has two sides of equal length")

class Quadrilateral(shapes):

        def __init__(self):
            self.sides = 4
        
        def description(self):
            print("All quadrilaterals have 4 sides and 4 angles")

class Square(Quadrilateral):

        def side_length(self, length):
            self.length = length
        
        def area(self):
            print( self.length * self.length)
        
        def perimeter(self):
            print(self.length * 4)
        
        def description(self):
            print("square is a quadrilateral with all the sides equal")

class Rectangle (Quadrilateral):

        def side_length(self, length, breadth):
            self.length = length
            self.breadth = breadth
        
        def area(self):
            print( self.length * self.breadth)
        
        def perimeter(self):
            print( (self.length  + self.breadth )* 2)
        
        def description(self):
            print("A quadrilateral whose opposite sides are equal")

class Circle(shapes):

        def __init__(self, center_x, center_y, radius):
            self.X = center_x
            self.Y = center_y
            self.radius = radius
        
        def description(self):
            print("Circle is the collection of the points which are equidistant from the center ")
        
        def area(self):
            print((self.pi) * (self.radius ** 2))
        
        def perimeter(self):
            print(2 * self.pi * self.radius)

class Ellipse(shapes):

        def __init__(self, center_x, center_y, major, minor):
            self.X = center_x
            self.Y = center_y
            self.major = major
            self.minor = minor
        
        def description(self):
            print("oval shaped circle")
        
        def area(self):
            print((self.pi) * (self.major)*(self.minor))
        
        def perimeter(self):
            square_root = (math.sqrt(self.major ** 2 + self.minor ** 2) * 0.5 )
            print(2 * square_root)
        

my_circle = Circle(300, 300 , 10)
my_circle.description()
my_circle.area()
my_circle.perimeter()      



        

