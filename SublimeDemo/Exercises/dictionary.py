# list work to store a particular type of data and a particular set of data
# dictionary allows you to store data with more detail
# dictionary consist of key value pairs

#	instructor = {"name": "Colt", "owns_dog": True, "num_courses": 4, "is_hilarious": False, 44: "my favorite number"}

#	for value in instructor.values():
#		print(value)

#	for value in instructor.keys():
#		print(value)

#	for value in instructor.items():
#		print(value)

#	for k,v in instructor.items():
#		print(f"keys is {k} and value is {v}")

# to look / test if variable is one of the values, type -> "name" in instructor.values()
# to look / test if variable is one of the keys, type -> "name" in instructor.keys()
# "name" in instructors -> by default, this test if it's in the keys

# dictionary methods

# d = dict(a=1, b=2, c = 3)

# fromkeys creates keyvalue pairs from csv values
# fromkeys: pass in an iterable collection and then a value ; it will go through an iterable collection and then assign a value

#	{}.fromkeys("a","b") # {'a':'b'}
#	{}.fromkeys(["email"], "uknown") # {'email' : 'unkown'}
#	{}.fromkeys("a", [1,2,3,4,5])


# get method retrieves a key in an object and return None instead of a KeyError if the key does not exist

# Pop method takes a single argument corresponding to a key and removes that key-value pari from the dictionary. Method requires you to provide the key of what you want to remove

# popitem() removes a key-value pair at random

# update method will update a set of key and values into another list



