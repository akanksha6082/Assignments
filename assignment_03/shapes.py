import math;
import turtle as tk;

class shapes:
	pi = math.pi;
	def draw(self):
		pass;

class line(shapes):
	
	def __init__(self, x0, y0, x1, y1):
		self.__x0 = x0
		self.__y0 = y0
		self.__x1 = x1
		self.__y1 = y1
	
	def draw(self):
		tk.color('white')
		tk.goto(self.__x0, self.__y0)
		tk.color('black')
		tk.goto(self.__x1, self.__y1)
		tk.exitonclick()

class point(shapes):

	def __init__(self, x0, y0):
		self.__x0 = x0
		self.__y0 = y0
		
	
	def draw(self):
		tk.color('white')
		tk.setx(self.__x0)
		tk.sety(self.__y0)
		tk.dot(5, 'black')
		tk.exitonclick()
	
class circle(shapes):

	def __init__(self, r0):
		self.__r0 = r0
		
	def draw(self):
		tk.color('orange')
		tk.circle(self.__r0)
		tk.exitonclick()
	def area():
		print((self.pi)*(self.__r0)**2)

class ellipse(shapes):
	
	def __init__(self, major, minor):
		self.__major = major
		self.__minor = minor
	
	def draw(self):
		tk.shape('circle')
		tk.shapesize(self.__major, self.__minor, 1)
		tk.color("orange")
		tk.exitonclick()

	def area(self):
		print((self.pi)*(self.__minor)*(self.__major))

class square(shapes):
	
	def __init__(self, side):
		self.__side = side
	
	def draw(self):
		for i in range(0, 4):
			tk.color('red')
			tk.forward(self.__side)
			tk.left(90)

	def area(self):
		print((self.__side)**2)


class rectangle(shapes):
	
	def __init__(self, length, breadth):
		self.__length = length
		self.__breadth = breadth
	
	def draw(self):
		for i in range(0,2):
			tk.color('purple')
			tk.forward(self.__length)
			tk.left(90)
			tk.forward(self.__breadth)
			tk.left(90)

	def area(self):
		print((self.__length) * (self.__breadth))


class polygon(shapes):
	
	def __init__(self, sides, length):
		self.__sides = sides
		self.__length = length
		self.__angle  = 360/self.__sides 
	
	def draw(self):
		for i in range(self.__sides):
			tk.color('orange')
			tk.forward(self.__length)
			tk.left(self.__angle)

class triangle(shapes):
	
	def __init__(self, length):
		self.__length = length
	
	def draw(self):
		for i in range(3):
			tk.color('yellow')
			tk.forward(self.__length)
			tk.left(60)

class parallelogram(shapes):

	def __init__(self, side1, side2, angle):
		self.__side1 = side1
		self.__side2 = side2
		self.__angle = angle
		
	
	def draw(self):
	
		tk.forward(self.__side1)
		tk.left(self.__angle)
		tk.forward(self.__side2)
		tk.left(180 - self.__angle)
		tk.forward(self.__side1)
		tk.left(self.__angle)
		tk.forward(self.__side2)
		
class spiral(shapes):
	
	def __init__(self, radius, angle, number):
		self.__radius = radius
		self.__angle = angle
		self.__number = number
	
	def draw(self):
		for i in range(self.__number):
	    		tk.circle(self.__radius + i)
	    		tk.right(self.__angle)


			
hexagon = polygon(6, 100)
hexagon.draw()	
			

		


	
	

