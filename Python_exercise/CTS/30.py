def safe_division(a, b):
    try:
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero")

safe_division(10, 2)