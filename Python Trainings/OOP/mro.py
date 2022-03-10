# Method Resolution Order (MRO)

# Order in which python will look for methods or instances of that class

# You can programmatically reference the MRO three ways:
	# 1. _mro_ attribute on the class 
	# 2. use the mro() method on the class
	# 3. use the builtin help(cls) method



class A:
	def do_something(self):
		print("Method Defined in A")

class B(A):
	pass
	# def do_something(self):
	# 	print("Method Defined in B")

class C(A):
	pass
	# def do_something(self):
	# 	print("Method Defined in C")

class D(B, C):
	pass
	# def do_something(self):
	# 	print("Method Defined in D")

# print(D.__mro__) # will tell us order of methods run
# print(D.mro())
# help(D)
thing = D()
thing.do_something()





























