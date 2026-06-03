def calculate():
    print("Select Operation: +, -, *, /")
    op = input("Enter operator: ")
    n1 = float(input("First number: "))
    n2 = float(input("Second number: "))

    if op == '+': print(n1 + n2)
    elif op == '-': print(n1 - n2)
    elif op == '*': print(n1 * n2)
    elif op == '/':
        print(n1 / n2 if n2 != 0 else "Error: Division by zero")
    else: print("Invalid Operator")

calculate()
