def divide(a,b):
	try:
		result = a/b
	except ZeroDivisionError:
		print("don't divide by zero please!!!")
	except TypeError as err:
		print("a and b must be ints or floats")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")

print(divide(1,2))
print(divide(1,'a'))




















