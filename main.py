history = []
try:
    with open("history.txt", "r") as file:
        history = file.read().splitlines()
except FileNotFoundError:
        history = []
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

def show_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("6. View calculation history")
    print("7. Clear calculation history")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            result = add(num1, num2)
            history.append(f"{num1} + {num2} = {result}")
            print("Result:", result)
            with open("history.txt", "a") as file:
                file.write(f"{num1} + {num2} = {result}\n")

        elif choice == "2":
            result = subtract(num1, num2)
            history.append(f"{num1} - {num2} = {result}")
            print("Result:", result)
            with open("history.txt", "a") as file:
                file.write(f"{num1} - {num2} = {result}\n")
        elif choice == "3":
            result = multiply(num1, num2)
            history.append(f"{num1} * {num2} = {result}")
            print("Result:", result)
            with open("history.txt", "a") as file:
                file.write(f"{num1} * {num2} = {result}\n")

        elif choice == "4":
            result = divide(num1, num2)
            history.append(f"{num1} / {num2} = {result}")
            print("Result:", result)
            with open("history.txt", "a") as file:
                file.write(f"{num1} / {num2} = {result}\n")

    elif choice == "6":
        if not history:
            print("No calculations yet.")
        else:
            print("\nCalculation History:")
            for i, item in enumerate(history, 1):
                print(f"{i}. {item}")
    elif choice == "7":
        if not history:
            print("History is already empty")
        else:
            confirm = input("Are you sure you want to clear history? (y/n): ").lower()
            if confirm == "y":
                history.clear()
                open("history.txt", "w").close()
                print("Calculation history cleared.")
                print("Calculation history cleared!")
            else:
                print("History not cleared.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
