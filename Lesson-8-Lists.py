

cities = ['New York', 'Moscvow', 'New delli', 'toronto']


print(len(cities))
print(cities[2].title())
print(cities[3].title())
print(cities[-1])  #last from the end


cities[2] = 'smila' #replace in list

print(cities[2].title())

cities.append('Kursk') #add in end of list
print(cities)

cities.insert(0, 'Feodora') #add in appropriate position
cities.insert(3, 'Buk')
print(cities)

del cities[1] #remove object in list
print(cities)
cities.remove('smila') # remove object by name
print(cities)

deleted_city = cities.pop()

print("Deleted city is " + deleted_city)
print(cities)

cities.sort() #sort by alphabet from A
print(cities)

cities.sort(reverse=True)  #sort by alphabet from Z
print(cities)

cities.reverse() #sort in opposite order
print(cities)


