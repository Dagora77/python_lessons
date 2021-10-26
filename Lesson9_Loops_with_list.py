cars = ['bmw', 'cars', 'mers', 'skoda', 'opel']

print(cars)

for car in cars:
    print(car.upper())

for x in range (1, 6):
    print(x)

mynumber_list = list(range(0, 10))
print(mynumber_list)
print("===============================")

for x in mynumber_list:
    x = x * 2
    print(x)

print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print("Max number is " + str(max(mynumber_list)))
print("Min number is " + str(min(mynumber_list)))
print("Sum of lis is " + str(sum(mynumber_list)))

print('=========================================')

cars = ['bmw', 'cars', 'mers', 'skoda', 'opel']

mycars = cars[1:3] #print list where 1 is start position and 3 elements numbers to print
print(mycars)
mycars = cars[:4] #cut to 4 position
print(mycars)

mycars = cars[-3:] #from -3 to end
print(mycars)

cars = ['bmw', 'cars', 'mers', 'skoda', 'opel']
mycars = cars[:] #copy list

