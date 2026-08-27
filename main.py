import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"
expenses = []


def load_expenses():
    global expenses
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            expenses = json.load(file)
    else:
        expenses = []


def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def get_next_id():
    if not expenses:
        return 1
    return max(e["id"] for e in expenses) + 1


def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: ₹"))
            if amount > 0:
                return round(amount, 2)
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid amount.")


def get_date():
    while True:
        date = input(
            "Enter date (YYYY-MM-DD) or press Enter for today: "
        ).strip()
        if not date:
            return datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def add_expense():
    print("\nAdd Expense")
    amount = get_amount()

    while True:
        category = input("Enter category: ").strip()
        if category:
            break
        print("Category cannot be empty.")

    while True:
        description = input("Enter description: ").strip()
        if description:
            break
        print("Description cannot be empty.")

    date = get_date()

    expense = {
        "id": get_next_id(),
        "amount": amount,
        "category": category,
        "description": description,
        "date": date,
    }

    expenses.append(expense)
    save_expenses()

    print("\nExpense added successfully!")
    print(f"Expense ID: {expense['id']}")


def view_expenses():
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\nAll Expenses")
    print(
        f"{'ID':<5}"
        f"{'Date':<15}"
        f"{'Category':<18}"
        f"{'Description':<25}"
        f"{'Amount':>12}"
    )

    for e in expenses:
        print(
            f"{e['id']:<5}"
            f"{e['date']:<15}"
            f"{e['category'][:16]:<18}"
            f"{e['description'][:23]:<25}"
            f"₹{e['amount']:>10.2f}"
        )


def find_expense(expense_id):
    for e in expenses:
        if e["id"] == expense_id:
            return e
    return None


def update_expense():
    if not expenses:
        print("\nNo expenses found.")
        return

    view_expenses()
    try:
        expense_id = int(input("\nEnter expense ID to update: "))
    except ValueError:
        print("Please enter a valid ID number.")
        return

    expense = find_expense(expense_id)
    if not expense:
        print("Expense not found.")
        return

    print("\nPress Enter to keep the current value.")

    amount = input(f"Amount [{expense['amount']}]: ₹").strip()
    if amount:
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be greater than 0.")
                return
            expense["amount"] = round(amount, 2)
        except ValueError:
            print("Invalid amount entered.")
            return

    category = input(f"Category [{expense['category']}]: ").strip()
    if category:
        expense["category"] = category

    description = input(f"Description [{expense['description']}]: ").strip()
    if description:
        expense["description"] = description

    date = input(f"Date [{expense['date']}] (YYYY-MM-DD): ").strip()
    if date:
        try:
            datetime.strptime(date, "%Y-%m-%d")
            expense["date"] = date
        except ValueError:
            print("Invalid date format. Update cancelled.")
            return

    save_expenses()
    print("Expense updated successfully!")


def delete_expense():
    if not expenses:
        print("\nNo expenses found.")
        return

    view_expenses()
    try:
        expense_id = int(input("\nEnter expense ID to delete: "))
    except ValueError:
        print("Please enter a valid ID number.")
        return

    expense = find_expense(expense_id)
    if not expense:
        print("Expense not found.")
        return

    print(
        f"\nYou are deleting: "
        f"₹{expense['amount']:.2f} | "
        f"{expense['category']} | "
        f"{expense['description']}"
    )

    confirm = input("Are you sure? (y/n): ").strip().lower()
    if confirm == "y":
        expenses.remove(expense)
        save_expenses()
        print("Expense deleted successfully!")
    else:
        print("Delete cancelled.")


def total_expense():
    if not expenses:
        print("\nNo expenses found.")
        return

    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal expenses: ₹{total:.2f}")


def filter_category():
    if not expenses:
        print("\nNo expenses found.")
        return

    category = input("\nEnter category: ").strip()
    found = [
        e for e in expenses if e["category"].lower() == category.lower()
    ]

    if not found:
        print("No expenses found for this category.")
        return

    print(f"\n{category} Expenses")
    total = 0

    for e in found:
        print(
            f"ID: {e['id']} | "
            f"₹{e['amount']:.2f} | "
            f"{e['description']} | "
            f"{e['date']}"
        )
        total += e["amount"]

    print(f"\nTotal for {category}: ₹{total:.2f}")


def monthly_summary():
    if not expenses:
        print("\nNo expenses found.")
        return

    while True:
        month = input("\nEnter month (1-12) or YYYY-MM: ").strip()
        try:
            if "-" in month:
                datetime.strptime(month, "%Y-%m")
                selected_month = month
            else:
                month_number = int(month)
                if month_number < 1 or month_number > 12:
                    print("Month must be between 1 and 12.")
                    continue
                selected_month = f"{datetime.now().year}-{month_number:02d}"
            break
        except ValueError:
            print("Invalid format. Try again.")

    monthly_expenses = [
        e for e in expenses if e["date"].startswith(selected_month)
    ]

    if not monthly_expenses:
        print(f"No expenses found for {selected_month}.")
        return

    total = sum(e["amount"] for e in monthly_expenses)
    print(f"\nSummary for {selected_month} ")

    for e in monthly_expenses:
        print(
            f"{e['date']} | "
            f"{e['category']} | "
            f"{e['description']} | "
            f"₹{e['amount']:.2f}"
        )

    print(f"Total: ₹{total:.2f}")


def category_summary():
    if not expenses:
        print("\nNo expenses found.")
        return

    categories = {}
    for e in expenses:
        category = e["category"]
        if category not in categories:
            categories[category] = 0
        categories[category] += e["amount"]

    print("\nCategory Summary")
    for category, total in sorted(
        categories.items(), key=lambda item: item[1], reverse=True
    ):
        print(f"{category:<20} ₹{total:.2f}")


def main():
    load_expenses()

    while True:
        print("\nEXPENSE TRACKER")
        print()
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Total Expenses")
        print("6. Filter by Category")
        print("7. Monthly Summary")
        print("8. Category Summary")
        print("9. Exit")
        print()

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                add_expense()
            case "2":
                view_expenses()
            case "3":
                update_expense()
            case "4":
                delete_expense()
            case "5":
                total_expense()
            case "6":
                filter_category()
            case "7":
                monthly_summary()
            case "8":
                category_summary()
            case "9":
                print("\nThank you for using Expense Tracker!")
                break
            case _:
                print("\nInvalid choice. Please choose 1-9.")


if __name__ == "__main__":
    main()