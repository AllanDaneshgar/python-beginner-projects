import json
from datetime import datetime
class Calc:
    def __init__(self):
        self.history = self.load_history()

    def load_history(self):
        try:
            with open("calculator/history.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_history(self):
        with open("calculator/history.json", "w", encoding="utf-8") as f:
            json.dump(self.history, f, indent=4, ensure_ascii=False)

    def add(self, num1, num2):
        result = num1 + num2
        operation = f"{num1} + {num2} = {result}"
        print(f"✅ Result: {operation}")
        self.record_history(operation)
        return result

    def minus(self, num1, num2):
        result = num1 - num2
        operation = f"{num1} - {num2} = {result}"
        print(f"✅ Result: {operation}")
        self.record_history(operation)
        return result

    def multi(self, num1, num2):
        result = num1 * num2
        operation = f"{num1} × {num2} = {result}"
        print(f"✅ Result: {operation}")
        self.record_history(operation)
        return result

    def division(self, num1, num2):
        if num2 == 0:
            print("❌ Error: Division by zero is not allowed!")
            return None

        result = num1 / num2
        operation = f"{num1} ÷ {num2} = {result:.2f}"
        print(f"✅ Result: {operation}")
        self.record_history(operation)
        return result

    def power(self, num1, num2):
        result = num1 ** num2
        operation = f"{num1}^{num2} = {result}"
        print(f"✅ Result: {operation}")
        self.record_history(operation)
        return result

    def square_root(self, num):
        if num < 0:
            print("❌ Error: Cannot calculate square root of negative number!")
            return None

        result = num ** 0.5
        operation = f"√{num} = {result:.2f}"
        print(f"✅ Result: {operation}")
        self.record_history(operation)
        return result

    def record_history(self, operation):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append({
            "timestamp": timestamp,
            "operation": operation
        })
        self.save_history()

    def show_history(self):

        print("\n" + "="*40)
        print("📜 CALCULATION HISTORY")
        print("="*40)

        if not self.history:
            print("No calculations yet!")
            return

        for i, record in enumerate(self.history, 1):
            print(f"{i}. [{record['timestamp']}] {record['operation']}")

        print("="*40)


def show_menu():

    print("="*30)
    print("🧮 CALCULATOR MENU")
    print("="*30)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Show History")
    print("8. Exit")
    print("="*30)

    try:
        choice = int(input("\nSelect operation (1-8): "))
        if 1 <= choice <= 8:
            return choice
        else:
            print("⚠️ Please choose a number from 1 to 8")
            return None
    except ValueError:
        print("⚠️ Please enter a valid number!")
        return None


def get_number(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️ Please enter a valid number!")


def main():

    print("="*40)
    print("🧮 WELCOME TO PYTHON CALCULATOR")
    print("="*40)

    calculator = Calc()

    while True:
        choice = show_menu()

        if choice is None:
            continue

        if choice == 8:
            print("\n👋 Thank you for using the calculator!")
            print("Goodbye! 👋")
            break

        if choice == 7:
            calculator.show_history()
            continue


        if choice == 6:
            num = get_number("Enter a number: ")
            calculator.square_root(num)

        else:
            print("\nEnter two numbers:")
            num1 = get_number("First number: ")
            num2 = get_number("Second number: ")

            if choice == 1:
                calculator.add(num1, num2)
            elif choice == 2:
                calculator.minus(num1, num2)
            elif choice == 3:
                calculator.multi(num1, num2)
            elif choice == 4:
                calculator.division(num1, num2)
            elif choice == 5:
                calculator.power(num1, num2)


if __name__ == "__main__":
    main()
import json
from datetime import datetime
class Calc:
    def __init__(self):
        self.history = self.load_history()

    def load_history(self):
        try:
            with open("./history.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_history(self):
        with open("./history.json", "w", encoding="utf-8") as f:
            json.dump(self.history, f, indent=4, ensure_ascii=False)

    def add(self, num1, num2):
        result = num1 + num2
        operation = f"{num1} + {num2} = {result}"
        print(f"✅ Result: {operation}")
        self.record_history(operation)
        return result

    def minus(self, num1, num2):
        result = num1 - num2
        operation = f"{num1} - {num2} = {result}"
        print(f"✅ Result: {operation}")
        self.record_history(operation)
        return result

    def multi(self, num1, num2):
        result = num1 * num2
        operation = f"{num1} × {num2} = {result}"
        print(f"✅ Result: {operation}")
        self.record_history(operation)
        return result

    def division(self, num1, num2):
        if num2 == 0:
            print("❌ Error: Division by zero is not allowed!")
            return None

        result = num1 / num2
        operation = f"{num1} ÷ {num2} = {result:.2f}"
        print(f"✅ Result: {operation}")
        self.record_history(operation)
        return result

    def power(self, num1, num2):
        result = num1 ** num2
        operation = f"{num1}^{num2} = {result}"
        print(f"✅ Result: {operation}")
        self.record_history(operation)
        return result

    def square_root(self, num):
        if num < 0:
            print("❌ Error: Cannot calculate square root of negative number!")
            return None

        result = num ** 0.5
        operation = f"√{num} = {result:.2f}"
        print(f"✅ Result: {operation}")
        self.record_history(operation)
        return result

    def record_history(self, operation):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append({
            "timestamp": timestamp,
            "operation": operation
        })
        self.save_history()

    def show_history(self):

        print("\n" + "="*40)
        print("📜 CALCULATION HISTORY")
        print("="*40)

        if not self.history:
            print("No calculations yet!")
            return

        for i, record in enumerate(self.history, 1):  
            print(f"{i}. [{record['timestamp']}] {record['operation']}")

        print("="*40)


def show_menu():

    print("="*30)
    print("🧮 CALCULATOR MENU")
    print("="*30)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Show History")
    print("8. Exit")
    print("="*30)

    try:
        choice = int(input("\nSelect operation (1-8): "))
        if 1 <= choice <= 8:
            return choice
        else:
            print("⚠️ Please choose a number from 1 to 8")
            return None
    except ValueError:
        print("⚠️ Please enter a valid number!")
        return None


def get_number(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️ Please enter a valid number!")


def main():

    print("="*40)
    print("🧮 WELCOME TO PYTHON CALCULATOR")
    print("="*40)

    calculator = Calc()

    while True:
        choice = show_menu()

        if choice is None:
            continue

        if choice == 8:
            print("\n👋 Thank you for using the calculator!")
            print("Goodbye! 👋")
            break

        if choice == 7:
            calculator.show_history()
            continue


        if choice == 6:
            num = get_number("Enter a number: ")
            calculator.square_root(num)

        else:
            print("\nEnter two numbers:")
            num1 = get_number("First number: ")
            num2 = get_number("Second number: ")

            if choice == 1:
                calculator.add(num1, num2)
            elif choice == 2:
                calculator.minus(num1, num2)
            elif choice == 3:
                calculator.multi(num1, num2)
            elif choice == 4:
                calculator.division(num1, num2)
            elif choice == 5:
                calculator.power(num1, num2)


if __name__ == "__main__":
    main()
