#Function Definitions
def circleArea(r):
    return r / (2 * 3.14159265358979)

def FtoC(f):
    return (f - 32) * 5 / 9

def averageOfThree(a, b, c):
    return (a + b + c) / 3

def start():
    print("1: circleArea\n2: FtoC\n3: AverageOfThree")
    function_type = int(input("Enter Selection: "))

    if function_type == 1:
        user_input = int(input("Enter circle radius: "))
        print("The area of the circle is", circleArea(user_input))
        start()
    elif function_type == 2:
        user_input = int(input("Enter farenheight temperature: "))
        print("The Celcius temperature is", FtoC(user_input))
        start()
    elif function_type == 3:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        number_3 = int(input("Enter third number: "))
        print("The average of", number_1, ",", number_2, "and", number_3, "is", averageOfThree(number_1, number_2, number_3))
        start()
    else:
        print("Invalid input.")
        start()

start()