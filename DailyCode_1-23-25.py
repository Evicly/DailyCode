#Function Definitions
def sphereSurfaceArea(r):
    return 4 * 3.14159265358979 * r * r

def ChangeChecker(n):
    if n % 5 == 0:
        print("you dont need pennies")
    else:
        print("you need dem pennies")
def primeNumber(n):
    if n > 1:
        for i in range (2, (n // 2) + 1):
            if (n % i) == 0:
                return True
            else:
                return False

def start():
    print("1: sphereSurfaceArea\n2: ChangeChecker\n3: primeNumber")
    function_type = int(input("Enter Selection: "))

    if function_type == 1:
        user_input = int(input("Enter sphere radius: "))
        print("The surface area of the sphere is", sphereSurfaceArea(user_input))
        start()
    elif function_type == 2:
        user_input = int(input("Enter number: "))
        ChangeChecker(user_input)
        start()
    elif function_type == 3:
        user_input = int(input("Enter number: "))
        print("Is", user_input, "prime number?", primeNumber(user_input))
        start()
    else:
        print("Invalid input.")
        start()

start()