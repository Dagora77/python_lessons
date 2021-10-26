
'''
name = input('Please enter your name: ')

print('Hello dear ' + name)

num1 = input("Enter x ")
num2 = input("Enter y ")

summa = int(num1) + int(num2)


print(summa)
message = ""

while True:
    message = input("Enter password ")
    if message == 'secret': break
    print(message + "Password not correct")

print('Password was: ' + message)
'''

mylist = []
msg = ''

while msg != 'stop'.upper():
    msg = input("Enter new item, and STOP to finish ")
    mylist.append(msg)

print(mylist)