#Function Definitions
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def isPalindrome(str):
    return str == str[::-1]

def pattern(n):
    if n > 0:
        print("*" * n)
        pattern(n - 1)


def start():
    print("1: factorial\n2: isPalindrome\n3: pattern")
    function_type = int(input("Enter Selection: "))

    if function_type == 1:
        user_input = int(input("Enter value: "))
        print("The factorial of", user_input, "is", factorial(user_input))
        start()
    elif function_type == 2:
        user_input = input("Enter word: ")
        print(user_input, "is a palindrome:", isPalindrome(user_input))
        start()
    elif function_type == 3:
        user_input = int(input("Enter number: "))
        pattern(user_input)
        start()
        start()
    else:
        print("Invalid input.")
        start()

start()