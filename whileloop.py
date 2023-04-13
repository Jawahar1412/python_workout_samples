x = 0
while x <= 10:
    print ("This line has been printed"),
    print (x),
    print ('times')
    x= x+1

def factorial(number):
    result = 1
    while int(number > 0):
        result = result*number
        number = number -1
    return result
in_variable = input("Enter the number")
print factorial(in_variable)
