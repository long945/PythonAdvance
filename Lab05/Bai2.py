from Continent import Continent
from Country import Country
#a
canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040,9826675)
mexico = Country('Mexico', 112336538, 1943950)

countries = [canada, usa , mexico]
north_america = Continent('North America', countries)

for country in north_america.countries:
    print(country)
#b
print(north_america.total_population())
#c 
print(north_america)