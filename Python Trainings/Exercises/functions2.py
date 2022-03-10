# *args stores info in a tuple

'''def sum_sum_all_nums(*args):
	total = 0
	for num in args:
		total += num
	return total

print(sum_sum_all_nums(4,6,9,4,10))
print(sum_sum_all_nums(4,6))'''

def ensure_correct_info(*args):
	if "Colt" in args and "Steele" in args:
		return "Welcome back Colt!"
	return "Not sure who you are ..."

print(ensure_correct_info(2,"nan","pop"))
print(ensure_correct_info(1,True, "Steele", "Colt"))

# **kwargs stores info in a dictionary


###
def fav_colors(**kwargs):
	for person, color in kwargs.items():
		print(f"{person}'s favorite color is {color}")
fav_colors(colt = "purple", ruby = "red", ethel = "teal")

###


def special_greeting(**kwargs):
	if "David" in kwargs and kwargs["David"] == "special":
		return "You get a special greeting David!"
	elif "David" in kwargs:
		return f"{kwargs['David']} David!"

	return "Not sure who this is..."

print(special_greeting(David='Hello'))
print(special_greeting(Bob='Hello'))
print(special_greeting(David='special'))	