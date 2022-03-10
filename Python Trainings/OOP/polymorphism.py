# Polymorphism
# an object can take on many shapes and forms

class Animal():
	def speak(self):
		raise NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
	def speak(self):
		return "woof"

class Cat(Animal):
	def speak(self):
		return "meow"

class Fish(Animal):
	pass

d = Dog()
print(d.speak())
f = Fish()
print(f.speak())


# Second type of Polymorphism is having the same operation work for different kinds of objects


















































































































