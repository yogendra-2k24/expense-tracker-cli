import json

expenses = []

def add_expense():
    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")
    
    expense = {
        "amount" : amount,
        "category" : category
    }

    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expense():
    if not expenses:
        print("No expenses found. \n")
        return
    
    print("\n--- Expense List ---")
    for expense in expenses:
        print(f"Amount: {expense["amount"]}")
        print(f"Category: {expense["category"]}")
        print("-" * 20)
        print()

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent = 4)

while True:
    print("==== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        save_expenses()
        print("Expenses saved to expenses.json")
        print("Exiting...")
        break

    else:
        print("invalid choice! Try again.\n")