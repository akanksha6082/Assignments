from abc import ABC, abstractmethod

class Animal:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@abstractmethod
	def features(self):
		pass

class Herbivores(Animal):

	def features(self, nature):
		print("name = {0})\nage = {1}".format(self.name, self.age))
	
	def set_nature(self, nature):
		self.nature = nature
	
	@abstractmethod
	def description(self):
		pass
	
	@abstractmethod
	def food(self):
		pass

class Giraffe(Herbivores):
	
	__species = 'mammal'

	def description(self):
		print ("Giraffe is herbivores and is tallest living terestial animal")
	
	def get_species(self):
		print(self.__species)
	
	def food(self):
		print("feed on leaves, shoots of the trees and shrubs")
	
	def speak(self, sound):
		print("{0} is making sound {1} {1}".format(self.name, sound))

	
class Hare(Herbivores):
	
	__species = 'mammal'

	
	def description(self):
		print ("Hare is fast running and is long eared mammal that resembles rabbit")
	
	def get_species(self):
		print(self.__species)
	
	def food(self):
		print("feed on mostly plant matters")
	
	
	def speak(self, sound = ""):
		print("{0} is making sound {1} {1}".format(self.name, sound))

	def get_nature(self):
		print(self.nature)

class Carnivores(Animal):
	
	def features(self, nature):
		print("name = {0})\n age = {1}".format(self.name, self.age))
	
	def set_nature(self, nature):
		self.nature = nature
	
	@abstractmethod
	def description(self):
		pass
	
	@abstractmethod
	def food(self):
		pass

class Lion(Carnivores):

	__species = 'mammal'

	def description(self):
		print("Lion is the carnivore and is species of the family Felidae")
	
	def food(self):
		print("feeds mostly on the meat !")
	
	def speak(self, sound = ""):
		print("{0} is making sound {1} {1}".format(self.name, sound))

	def get_nature(self):
		print(self.nature) 
	
	def get_species(self):
		print(self.__species)

class Tiger(Carnivores):

	__species = 'mammal'

	def description(self):
		print("Tiger is the carnivore and is species of the family Felidae")
	
	def food(self):
		print("feeds mostly on the meat !")
	
	def speak(self, sound = ""):
		print("{0} is making sound {1} {1}".format(self.name, sound))

	def get_nature(self):
		print(self.nature) 
	
	def get_species(self):
		print(self.__species)

class Omnivores(Animal):

	def features(self):
		print("name = {0}\nage = {1}".format(self.name, self.age))
	
	def set_nature(self, nature):
		self.nature = nature
	
	@abstractmethod
	def description(self):
		pass
	
	@abstractmethod
	def food(self):
		pass

class Polar_bear(Omnivores):

	__species = 'marine mammals'

	def description(self):
		print("Bear is Omnivores Animal")
	
	def food(self):
		print("Bear mostly feed on the seals !")
	
	def speak(self, sound = ""):
		print("{0} is making sound {1} {1}".format(self.name, sound))

	def get_nature(self):
		print(self.nature) 
	
	def get_species(self):
		print(self.__species)

class Human(Omnivores):

	__species = 'terrestial mammals'

	def description(self):
		print("Homo sapiens is the only extant human species")
	
	def food(self):
		print("{0} both carnivorous and as well as herbivorous".format(self.name))
	
	def speak(self, sound = "talking"):
		print("{0} is  {1} ".format(self.name, sound))

	def get_nature(self):
		print(self.nature) 
	
	def get_species(self):
		print(self.__species)

human = Human("Tony", 25)
human.features()
human.description()
human.food()
human.speak()
human.speak("laughing")
human.set_nature("intelligent")
human.get_nature()
human.get_species()

	


