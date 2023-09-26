a, b = int(input('Enter first number: ')), int(input('Enter second number: '))
act = input('Enter operation: ')
if act == '+':
    print(f'Result: {a + b}')
elif act == '-':
    print(f'Result: {a - b}')
elif act == '*':
    print(f'Result: {a * b}')
elif act == '/':
    print(f'Result: {a / b}')
else:
    print('Incorrect input')