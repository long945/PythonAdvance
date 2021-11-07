from Country import Country
#a
canada = Country('Canada', 34482779, 9984670)
print('canada.name ->',canada.name)
print('canada.population ->',canada.population)
print('canada.area ->',canada.area)
#b
canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040, 9826675)
print('canada.is_larger(usa) -> ',canada.is_larger(usa))
#c
print('canada.population_density() ->', canada.population_density())
#d
usa = Country('United States of America', 313914040, 9826675)
print('usa ->',usa)
#e
canada = Country('Canada', 34482779, 9984670)
canada
print(canada)
[canada]
print([canada])