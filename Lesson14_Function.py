


def say_Hello(name):
    '''Print Hello'''
    print('Hello mr ' + name)

def aaaaa():
    print(('AAAAA'))


say_Hello("Saha")
aaaaa()
say_Hello("Pidor")

def summa(x, y):
    s = x + y
    return s

summa(2, 5)


x = summa(33, 25)

print(x)

def summa(x, y):
    return x + y

def factorial(x):
    """Calculate Factorial of Number X"""
    answer = 1
    for i in range (1, x + 1):
        answer = answer * i
    return answer

print(factorial(1))
print(factorial(5))

#2! = 1 * 2
#3! = 1 * 2 * 3
#4! = 1 * 2 * 3 * 4

for i in range (1, 10):
    print(str(i) + '!\t = ' + str(factorial(i)))

