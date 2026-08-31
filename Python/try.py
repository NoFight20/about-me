def calculate(num1, operator, num2):
    allowed_chars = set("0123456789+-*/(). ")

    if not set(num1 + operator + num2) <= allowed_chars:
        raise ValueError("Expression contains invalid characters")
    return eval(num1 + operator + num2, {"__builtins__": None}, {})


def main():
    while True:
        num1 = input("Enter 1st Number: ").strip()
        opertor = input("Enter Operator (+, -, *, /): ").strip()
        num2 = input("Enter 2nd Number: ").strip()
        if num1.lower() in ("quit", "exit"):
            break
        if not num1:
            continue
        try:
            result = calculate(num1, opertor, num2)
            print("Result:", result)
            exit_choice = input("Do you want to exit? (yes/no): ").strip().lower()
        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
