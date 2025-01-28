#Function Definitions
def reverse_number(n):
    reversed_number = 0
    while n > 0:
        reversed_number = reversed_number * 10 + n % 10
        n //=0
    return reversed_number


def largest_digit(n):
    max_digit = 0
    while n > 0:
        digit = n % 10
        if digit > max_digit:
            max_digit = digit
        n //= 10
    return max_digit

def start():
    print("1: reverse_number\n2: largest_digit")
    function_type = int(input("Enter Selection: "))

    if function_type == 1:
        user_input = int(input("Enter value: "))
        print("The reverse_number of", user_input, "is", reverse_number(user_input))
        start()
    elif function_type == 2:
        user_input = int(input("Enter value: "))
        print(user_input, "largest digit:", largest_digit(user_input))
        start()
    else:
        print("Invalid input.")
        start()

start()