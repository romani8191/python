try:
    f=open('C:\\Users\\Lenovo\\Desktop\\art\\rel\\file1.txt','w')
    f.write('Hi there , I am performing exception handling :)\n')
except IOError:
    print("Error:can't find the file")
else:
    print("Written content in the file successfully")
    f.close()

try:
    with open('C:\\Users\\Lenovo\\Desktop\\art\\rel\\file1.txt','a+') as f:
        f.write('I am back with a bang! ;)')
        a=f.readlines()
        print(a)

except IOError:
    print("Error:can't find the file")
else:
    print("Written content in the file successfully")



class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")

except InvalidAgeException:
    print("Exception occurred: Invalid Age")

