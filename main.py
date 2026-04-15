print("Tiny Calculator")

while True:
    print("\nOperations: +, -, *, /")
    operation = input("Choose operation: ")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if operation == "+":
        result = num1 + num2
        print("Result:", result)
    elif operation == "-":
        result = num1 - num2
        print("Result:", result)
    elif operation == "*":
        result = num1 * num2
        print("Result:", result)
    elif operation == "/":
        if num2 == 0:
            print("You cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print("Invalid operation")

    again = input("Do you want another calculation? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye.")
        break
