#Julian & Evan

#Function Definitions
def CircleCircumference(r):
    return r * (2 * 3.14159265358979)

def isEven(f):
    if f % 2:
        return False
    else:
        return True

def frog(a):
    for i in range(a):
        print("ribbit")

def start():
    print("1: CircleCircumference\n2: isEven\n3: frog")
    function_type = int(input("Enter Selection: "))

    if function_type == 1:
        user_input = int(input("Enter circle radius: "))
        print("The circumference of the circle is", CircleCircumference(user_input))
        start()
    elif function_type == 2:
        user_input = int(input("Enter number: "))
        print(user_input, "is even:", isEven(user_input))
        start()
    elif function_type == 3:
        user_input = int(input("Enter number: "))
        frog(user_input)
        start()
        start()
    else:
        print("Invalid input.")
        start()

start()