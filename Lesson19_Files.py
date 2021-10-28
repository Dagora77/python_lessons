

inputfile = '../Files/passwd.txt' #folder in upper directory
outputfile = '../Files/my_passwd.txt'

myfile = open(inputfile, mode='r', encoding="utf_8")
myfile2 = open(outputfile, mode='a', encoding="utf_8") # w - write a - attend

passwd_for_search = 'lol'
#for line in myfile:
#    print('Hello ' + line.strip()) #print by line

#for num, line in enumerate(myfile, 1):
#    print('Line # ' + str(num) + " : " + line.strip()) #calculate lines

#for num, line in enumerate(myfile, 1):
#   if 'xxx' in line:
#       print('Line # ' + str(num) + " : " + line.strip())



for num, line in enumerate(myfile, 1):
   if passwd_for_search in line:
       print('Line # ' + str(num) + " : " + line.strip())
       myfile2.write("Found password " + line)

myfile.close()
myfile2.close()

