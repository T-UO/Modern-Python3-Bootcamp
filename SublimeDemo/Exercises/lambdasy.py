def square(num): return num*num
square2 = lambda num: num * num # square2 function has no name. some languages call them anonymous functions
print(square2(7))

add = lambda a,b: a + b

print(square.__name__)
print(square2.__name__)
print(add.__name__)


# maps accepts at least two functions

# filter
# filter allows us to take a list, collection, list, or tuple and filter out specific items we want

l = [1,2,3,4]

evens = list(filter(lambda x: x % 2 == 0, l))

evens