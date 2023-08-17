import calculator_art as cal

def calculation(num1, operation, num2):
    if operation == "*":
        return num1 * num2
    elif operation == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return None
    elif operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2

print(cal.logo)
def calculator():
    num1 = float(input("Enter the first number: "))
    while True:
        operation = input("Enter the operation you want. ( * | / | + | - )\nOperation: ")
        num2 = float(input("Enter the next number: "))
        
        result = calculation(num1, operation, num2)
        
        if result is not None:
            print(f"{num1:g} {operation} {num2:g} = {result:g}")
        else: 
            print(f"\nUndefined.\n")
            calculator()
        
        if input(f"\nType 'y' to continue calculating with {result:g}, type 'n' to start a new calculation. ") == 'y':
            num1 = result
        else:
            calculator()

calculator()