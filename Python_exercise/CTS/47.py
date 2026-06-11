def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Invalid operator"

    except ZeroDivisionError:
        return "Cannot divide by zero"

print(calculate(10, 5, "+"))
print(calculate(10, 5, "-"))
print(calculate(10, 5, "*"))
print(calculate(10, 5, "/"))