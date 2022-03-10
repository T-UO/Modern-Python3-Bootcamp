# _name this is a private variable, property, or method; just for convention
# __name it changes the name; it's called name mangling; it puts the class name first
# __name__ used for pthon specific mehtods that are self-defined; convention should be respected

class Person:
	def __init__(self):
		_secret = 'hi!'
		self.secret = 'hi!'
		self.__msg = "I like turles!"
	# def doorman(self, guess):
	#	if guess == self._secret:
	#		let them in

p = Person()
print(p.name)
print(p._secret)
# print(dir(p))
print(p.__Person__msg)
print(p.__Person__lol)