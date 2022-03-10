# *args exercises / practice
# args accepts positional arguments
# the single asterisk operator can be used on any iterables that Python provides

'''

def my_sum(my_integers):
	result = 0
	for x in my_integers:
		result += x
	return result
 

integers = [1,2,3]
print(my_sum(integers))

def my_sum(*args):
	result = 0
	for x in args:
		result += x
	return result

print(my_sum(1,2,3,4))

def my_sum(*integers):
	result = 0
	for x in integers:
		result += x
	return result

print(my_sum(6,7,8,9))

# **kwargs accepts keyword arguments
# the double asterisk operator can only be used on dictionaries

def concatenate(**words):
	result = ""
	for arg in words.values():
		result += arg
	return result

print(concatenate(a="real",b="python",c="is",d="great")) '''

'''my_list = [1,2,3]

print(*my_list)'''

'''def my_sum(a,b,c):
	print(a+b+c)

my_list = [1,2,3,4]
my_sum(*my_list) '''

# When you use the * operator to unpack a list and pass arguments to a function, 
# it’s exactly as though you’re passing every single argument alone.

'''def combine_words(word,**kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    return word'''

 #   max(names, key = lambda n: len(n))

