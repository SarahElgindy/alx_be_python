def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def calculator():
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    operation = input("Choose the operation (+, -, *, /): ")

    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}")
        case "-":
            result = num1 - num2
            print(f"The result is {result}")
        case "*":
            result = num1 * num2
            print(f"The result is {result}")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}")
        case _:
            print("Invalid operation. Please choose one of +, -, *, or /.")

if __name__ == "__main__":
    calculator()
