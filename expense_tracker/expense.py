import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class ExpenseTracker:
    def __init__(self, file_name="expense.json"):
        self.filename = os.path.join(BASE_DIR, file_name)
        self.expenses = []
        self.load_expense()

    def load_expense(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    self.expenses = json.load(file)
                print(f"📂 Loaded {len(self.expenses)} expenses")
            except Exception as e:
                print(f"⚠️ Could not load expenses: {e}. Starting fresh.")
                self.expenses = []
        else:
            print("📝 No expenses file found. Starting fresh.")
            self.expenses = []

    def save_expense(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.expenses, file, indent=2, default=str, ensure_ascii=False)
        print("💾 Expenses saved!")

    def get_new_id(self):
        if self.expenses:
            return max(exp.get("id", 0) for exp in self.expenses) + 1
        else:
            return 1

    def add_expense(self):
        while True:
            type_e = input("Type (income/expense): ").strip().lower()
            if type_e not in ["income", "expense"]:
                print("❌ Input must be either income or expense!")
                continue
            break

        while True:
            amount_input = input("Amount: ").strip()
            if not amount_input:
                print("❌ Amount cannot be empty!")
                continue
            try:
                amount = float(amount_input)
                if amount <= 0:
                    print("❌ The value must be greater than 0!")
                    continue
                break
            except ValueError:
                print("❌ Amount must be a number!")

        while True:
            category = input("Category: ").strip().lower()
            if not category:
                print("❌ Category cannot be empty!")
                continue
            break

        while True:
            description = input("Description: ").strip()
            if description:
                break
            con = (
                input("Are you sure you don't want a description? (y/n) ")
                .strip()
                .lower()
            )
            if con == "y":
                description = ""
                break
            elif con == "n":
                continue
            else:
                print("Enter y to Yes and n to No!")

        while True:
            date_input = input(
                "Enter transaction date (YYYY-MM-DD, leave empty for today): "
            ).strip()
            if not date_input:
                transaction_date = datetime.now().strftime("%Y-%m-%d")
                break
            try:
                transaction_date = datetime.strptime(date_input, "%Y-%m-%d").strftime(
                    "%Y-%m-%d"
                )
                break
            except ValueError:
                print("❌ Invalid date format! Use YYYY-MM-DD")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_expense = {
            "id": self.get_new_id(),
            "type": type_e,
            "amount": amount,
            "category": category,
            "description": description,
            "date": transaction_date,
            "created_at": current_time,
            "updated_at": current_time,
        }

        self.expenses.append(new_expense)
        self.save_expense()
        print(f"✅ Expense added (ID: {new_expense['id']})")

    def show_all_expense(self):
        print("\n💰 ALL EXPENSES")
        print("=" * 40)
        if not self.expenses:
            print("No expenses yet!")
            return
        sorted_expenses = sorted(self.expenses, key=lambda x: x["id"])
        for expense in sorted_expenses:
            print(f"ID: {expense['id']}")
            print(f"Type: {expense['type']}")
            print(f"Amount: {expense['amount']:.2f}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print(f"Date: {expense['date']}")
            print(f"Created_at: {expense['created_at']}")
            print(f"Updated_at: {expense['updated_at']}")
            print("-" * 20)

    def delete_expense(self):
        print("\n🗑️ DELETE Expense")
        self.show_all_expense()
        try:
            expense_id = int(input("\n Enter Expense ID to delete: "))
        except ValueError:
            print("❌ Please enter a number!")
            return

        for i, expense in enumerate(self.expenses):
            if expense["id"] == expense_id:
                confirm = input(f"Delete {expense['description']}? (y/n): ").lower()
                if confirm == "y":
                    del self.expenses[i]
                    self.save_expense()
                    print("✅ Expense deleted!")
                else:
                    print("❌ Deletion cancelled!")
                return

        print(f"❌ Expense with ID {expense_id} not found!")

    def edit_expense(self):
        print("\n✏️ EDIT Expense")
        self.show_all_expense()
        try:
            expense_id = int(input("\nEnter expense ID to edit: ").strip())
        except ValueError:
            print("❌ Please enter a number!")
            return

        for expense in self.expenses:
            if expense["id"] == expense_id:
                print(f"\nEditing Expense ID: {expense_id}")

                while True:
                    new_type = input(f"Type [{expense['type']}]: ").strip().lower()
                    if not new_type:
                        break
                    if new_type not in ["income", "expense"]:
                        print("❌ Input must be either income or expense!")
                        continue
                    expense["type"] = new_type
                    break

                while True:
                    n_amount_input = input(f"Amount [{expense['amount']}]: ")
                    if not n_amount_input:
                        break
                    try:
                        new_amount = float(n_amount_input)
                        if new_amount <= 0:
                            print("❌ The value must be greater than 0!")
                            continue
                        expense["amount"] = new_amount
                        break
                    except ValueError:
                        print("❌ Amount must be a number!")

                while True:
                    new_Category = (
                        input(f"Category [{expense['category']}]: ").strip().lower()
                    )
                    if not new_Category:
                        break
                    expense["category"] = new_Category
                    break

                while True:
                    new_description = (
                        input(f"Description [{expense['description']}]: ")
                        .strip()
                        .lower()
                    )
                    if not new_description:
                        break
                    expense["description"] = new_description
                    break

                while True:
                    n_date_input = input(
                        "Enter transaction date (YYYY-MM-DD, leave empty for today): "
                    )
                    if not n_date_input:
                        transaction_date = datetime.now().strftime("%Y-%m-%d")
                        expense["date"] = transaction_date
                        break
                    try:
                        transaction_date = datetime.strptime(
                            n_date_input, "%Y-%m-%d"
                        ).strftime("%Y-%m-%d")
                        expense["date"] = transaction_date
                        break
                    except ValueError:
                        print("❌ Invalid date format! Use YYYY-MM-DD")

                expense["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_expense()
                print("✅ Expense partially updated!")
                return

        print("❌ Expense ID not found!")


def show_menu():
    print("\n" + "=" * 35)
    print("💰 EXPENSE TRACKER MENU")
    print("=" * 35)
    print("1. ➕ Add new expense")
    print("2. 👀 View all expenses")
    print("3. ✏️ Edit expense")
    print("4. 🗑️ Delete expense")
    print("5. 🔍 Search / Filter expenses")
    print("6. 📊 Show statistics")
    print("7. 📤 Export to CSV")
    print("8. 🚪 Exit")
    print("-" * 35)
    try:
        choice = int(input("Choose (1-8): ").strip())
        if 1 <= choice <= 8:
            return choice
        return None
    except ValueError:
        return None


def main():
    print("=" * 50)
    print("WELCOME TO EXPENSE TRACKER")
    print("Expenses are saved in 'expense.json'")
    tracker = ExpenseTracker()

    while True:
        choice = show_menu()
        if choice == 1:
            tracker.add_expense()
        elif choice == 2:
            tracker.show_all_expense()
        elif choice == 3:
            tracker.edit_expense()
        elif choice == 4:
            tracker.delete_expense()
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 8:
            print("\n👋 Goodbye!")
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("⚠️ Please choose a valid option (1-8)")


if __name__ == "__main__":
    main()
