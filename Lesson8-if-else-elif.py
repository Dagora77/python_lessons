


x = 27


if x == 25:
    print("Yes, you are right")
else:
    print('You are wrong')


age = 50

if age <= 4:
    print("Baby")
elif (age >= 4 and age <= 12):
    print("You are pizduk")
elif age >= 12 and age <= 21:
    print("You are young")
else:
    print("You are dead man")


print("===================================")

all_cars = ['bmw', 'ferrary', 'opel', 'dodge', 'toyota', 'mers', 'pego', 'lada']
german_cars = ['bmw', 'opel', 'mers']

if 'lada' in all_cars:
    print('Yes Lada in the list')
else:
    print('There is no lada')


for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx.title() + " is German car")
    else:
        print(xxxx.title() + " is not German car")



