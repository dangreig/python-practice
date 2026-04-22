import json


def show_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Remove Expense")
    print("5. Save and Exit")


def add_expense(expenses):
    date = input("Enter date (DD-MM-YYYY)")
    category = input("Enter category ")

    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Please enter a valid number")

    description = input("Enter description ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description,
    }

    expenses.append(expense)
    print("Expense Added")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded")
        return

    print("\nExpenses:")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['date']} | "
            f"{expense['category']} | "
            f"£{expense['amount']:.2f} | "
            f"{expense['description']}"
        )


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Spent: £{total:.2f}")


def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return


def remove_expense(expenses):
    if not expenses:
        print("No expenses to remove.")
        return

    print("\nExpenses:")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index:<3} "
            f"{expense['date']:<12} "
            f"{expense['category']:<15} "
            f"£{expense['amount']:<10.2f} "
            f"{expense['description']}"
        )

    while True:
        choice = input("\nEnter the number of the expense to remove: ")

        try:
            expense_index = int(choice) - 1

            if 0 <= expense_index < len(expenses):
                removed = expenses.pop(expense_index)
                print(
                    f"Removed: {removed['date']} | "
                    f"{removed['category']} | "
                    f"£{removed['amount']:.2f} | "
                    f"{removed['description']}"
                )
                break
            else:
                print("That number is not in the list.")

        except ValueError:
            print("Please enter a valid whole number.")


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            remove_expense(expenses)
        elif choice == "5":
            save_expenses(expenses)
            print("Expenses saved. Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


main()
