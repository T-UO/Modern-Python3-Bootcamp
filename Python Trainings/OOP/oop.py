class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

user1 = User("joe", "smith", 86) # we are instantiating a new user or creating an object / instance of user
user2 = User("blanca", "alexis", 90)


print(user1.first, user1.last, user1.age)


# give an instance of a class or a class attributes




# object oriented programming is a method of programming that attempts to model some processes or things in the world as a class or object

# a class is a blueprint for objects. Classes can contain methods (functions) and attributes (similar to keys in a dict)

# instance - objects that are constructed from a class blueprint that contain their class's methods and properties

# The bulk of the challenge w/ OOP comes with determining what needs to be its own class

# Python does not actually support true private or public variables, attributes, or methods

# _cards is an example of a private list attribute; it's not actually private but just a conventional style to let other developers know that this variable should only be used within this class

