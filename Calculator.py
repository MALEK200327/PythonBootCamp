
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

def calculator():
    close_calculator = False
    num1 = float(input("Enter the first number: \n"))
    while not close_calculator:
        for symbol in operations:
            print(symbol)
        operation = input("Enter operation: \n")
        num2 = float(input("Enter the second number: \n"))
        if operation in operations:
            answer = operations[operation](num1, num2)
            print(f"{num1} {operation} {num2} = {answer}")
            reset_calculator = input("Enter 'Y' to continue with the previous number or 'N' to start a new calculation: ").upper()
            if reset_calculator == "Y":
                num1 = answer
            elif reset_calculator == "N":
                close_calculator = True
                print("\n" * 20)  # Clear the console
                calculator()
            else:
                print("Invalid input. Exiting calculator.")
                close_calculator = True
        else:
            print("Invalid operation. Please select a valid operation.")

calculator()



