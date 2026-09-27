a = float(input("Enter the 1st num: "))
b = float(input("Enter the 2nd num: "))
op = input("Enter Operater ( +, -, *, /, % **): ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
elif op == '%':
    print(a % b)
elif op == '**':
    print(a ** b)
else:
    print("INVAILD OPERATION")