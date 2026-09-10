def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def main():
    print("=== Simple Calculator ===")
    print("Operations: +  -  *  /")
    print("Type 'quit' to exit\n")

    while True:
        user_input = input("Enter calculation (e.g. 5 + 3): ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        parts = user_input.split()

        if len(parts) != 3:
            print("Please enter in the format: number operator number\n")
            continue

        num1_str, operator, num2_str = parts

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("Both values must be numbers.\n")
            continue

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            print("Unknown operator. Use one of: + - * /\n")
            continue

        print(f"Result: {result}\n")


if __name__ == "__main__":
    main()
