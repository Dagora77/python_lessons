import sys

filename = '../Files/passdwd.txt'
while True:
    try:
        print("Inside try")
        myfile = open(filename, mode='r', encoding='utf_8')
    except Exception:
        print("Inside EXCEPT")
        print("Error found!")
        print(sys.exc_info()[1])
        filename = input("Enter correct file name! : ")
#    sys.exit()
    else:
        print("Inside ELSE")
        print(myfile.read())
        sys.exit()


print("==================EOF========================")

