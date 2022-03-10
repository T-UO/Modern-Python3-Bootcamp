class Animal:
	cool = True

	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animals says {sound}")

class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species = "Cat") # super() refers to the class Animal or base class
		self.breed = breed
		self.toy = toy
	def play(self):
		print(f"{self.name} plays with {self.toy}")
	



blue = Cat("Blue", "Scottish Fold", "String")
print(blue)
print(blue.species)
print(blue.breed)
print(blue.toy)
blue.play()

# Animal
# 	species
# 	name

# Cat
# 	species
# 	name
# 	breed
# 	favorite_toy















