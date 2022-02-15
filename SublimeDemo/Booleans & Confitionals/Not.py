# use not to negate other pieces of logic

age = 7

# 2-8 results in $2 ticket
# > 65 results in $5 ticket
# Other people will pay $10

if not ((age >= 2 and age <=8) or age >=65):
	print('you pay $10 and are not a child or senior')
else:
	print('You are a child or senior')


