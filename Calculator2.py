# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# This function calculates the square of a number
def square(x):
    return x ** 2

# This function calculates the square root of a number
def square_root(x):
    if x >= 0:
        return x ** 0.5
    else:
        return "Invalid input for square root"

# This function calculates the power of a number to another
def power(x, y):
    return x ** y

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Square Root")
print("7. Power")

while True:
    # take input from the user
    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    # check if choice is one of the seven options
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        try:
            num1 = float(input("Enter first number: "))
            if choice != '5' and choice != '6':
                num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print("Square of", num1, "=", square(num1))

        elif choice == '6':
            print("Square root of", num1, "=", square_root(num1))

        elif choice == '7':
            print(num1, "to the power of", num2, "=", power(num1, num2))

        # check if user wants another calculation
        next_calculation = input("Do another calculation? (yes/no): ")
        if next_calculation.lower() != "yes":
            print("Exiting calculator.")
            break

    else:
        print("Invalid Input")
