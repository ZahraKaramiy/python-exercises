def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Division by zero")
        return None
        
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = divide(num1, num2)
        if result is not None:
            print("Result:", result)
            break
    
    except ValueError:
        print("Error!! Please enter only numbers.")
        
    finally:
        print("The program was successfully done!")