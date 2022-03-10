# inheritance allows us to define a class that inherits functionality from another class
# in python inheritance works by passing the parent class as an argument to the definition of a child class

class Animal:   # This is the base class

	cool = True

	def make_sound(self, sound):
		print(f"this animal says {sound}")

class Cat(Animal): # if we pass in an argument like this, it tells python that Cat inherits from the animal class
	pass 

#	a = Animal()
#	a.make_sound("Chirp")

blue = Cat()
#	print(blue.cool)
#	blue.make_sound("meow")

print(isinstance(blue, object))