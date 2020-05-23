class Animal:
	
	def __init__(self, name, colour):
		self.__eyes = 2
		self.__tail = 1
		self.__legs = 4
		self.name = name
		self.colour = colour
	
	def speak(self):
		print("Animal is speaking");

	def info(self):
		print("eyes = {0}\ntail = {1}\nlegs = {2}".format(self.__eyes, self.__tail, self.__legs))
		print("name = {0}\ncolour = {1}".format(self.name, self.colour))
	


class Dog(Animal):
	
	species = "mammal"

	def speak(self):
		print ("Barking")
	
	def change_colour(self, colour):
		self.colour = colour
	
	def change_name(self, name):
		self.name = name
	
	def move(self):
		print ("running")

class Cat(Animal):
	
	species = "mammal"

	def speak(self):
		print ("Meow Meow")
	
	def move(self):
		print ("{0} is Walking".format(self.name))
	
	def drink(self):
		print("{0} is drinking milk".format(self.name))
	
class Lion(Animal):
	
	species = "mammal"

	def move(self):
		print("chasin a deer")

	def speak(self):
		print ("Roaring")

	def eat(self):
		print ("Eating meat..")

class Monkey(Animal):

	def speak(self):
		print ("whoop whoop")
	def eat(self):
		print ("eating banana")
	def move(self):
		print ("Jumping")

class Horse(Animal):	
	
	species = "mammal"

	def speak(self):
		print ("Neighing")
	def move(self):
		print ("Running ...")
	def eat(self):
		print ("Eating hay")

class Zebras(Animal):
	
	species = "mammal"

	def speak(self):
		print ("Whinny..")
	def move(self):
		print ("crossing")
	def eat(self):
		print ("Having Grass..")

class Rabbit(Animal):
	
	species = 'mammal'
	
	def speak(self):
		print ("Squeak Squeak !!")

	def move(self):
		print ("Running ...")

	def eat(self):
		print ("Eating hay, fresh veggies and fruits..")

class Sheep(Animal):

	species = 'mammal'
	
	def speak(self):
		print ("Bleat Bleat!!")

	def move(self):
		print ("Following the Folk")

	def eat(self):
		print ("Eating Pasture and legumes")

class Human(Animal):
	
	species = 'mammal'
	
	def speak(self):
		print ("{0} is taking".format(self.name))

	def move(self):
		print ("can run and walk !!")

	def eat(self):
		print ("Eating a diet food !")

class Elephant(Animal):
	
	species = 'mammal'
	
	def speak(self):
		print ("{0} is trumping".format(self.name))

	def move(self):
		print ("Walking ..")

	def eat(self):
		print (" Eating grass, fruits, twigs..")
	
	
	
		

rabbit = Rabbit("Oreo", "white")
rabbit.move()
print (rabbit.species)
rabbit.speak()
rabbit.eat()
rabbit.info()
	

	
	
	


