expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)
        print("Expense added successfully!")

    elif choice == "2":
        if expenses:
            print("\nExpenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. ₹{expense}")
        else:
            print("No expenses recorded.")

    elif choice == "3":
        total = sum(expenses)
        print(f"Total Expenses: ₹{total}")

    elif choice == "4":
        print("Exiting Expense Tracker...")
        break

    else:
        print("Invalid choice! Please try again.")