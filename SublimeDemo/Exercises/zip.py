# Makes an iterator that aggregates elements from each of the iterables

first_zip = zip([1,2,3], [4,5,6])

list(first_zip) # [(1,4), (2,5), (3,6)]

dict(first_zip) # {1: 4, 2: 5, 3: 6}

# can also use the star operator to unpack a list and zip items

five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]

list(zip(*five_by_two))

[pair for pair in zip(mid)]

midterms = [80, 91, 78]

finals = [98, 89, 53]

students = ['dan', 'ang', 'kate']

# final_grades = {'dan': 98, 'ang': 91, 'kate': 78}

final_grades = {t[0]: max(t[1], t[2]) for t in zip(students,midterms, finals)}
print(final_grades)

scores = 
dict(
zip(students,
map(
lambda pair: max(pair),
zip(midterms, finals)
)))

print(dict(scores))