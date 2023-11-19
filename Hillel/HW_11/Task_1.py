def arithmetic(a, b, operation):
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        try:
            result = a / b
        except ZeroDivisionError:
            result = "Division by zero"
    else:
        result = f"Not known operation: {operation}"
    return result


print(arithmetic(1, 2, '+'))
