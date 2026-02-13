import json
from datetime import datetime

class Contact():
    def __init__(self, file_name=".contact.json"):
        self.filename = file_name
        self.contacts = []
        self.load_contacts()

def show_menu():
    print("\n" + "-"*30)
    print("1. ➕ Add new contact")
    print("2. 👥 View all contacts")
    print("3. 🔍 Search contacts")
    print("4. 🗑️ Delete contact")
    print("5. 🚪 Exit")

    try:
        choice = int(input("Choose (1-7): "))
        return choice if 1 <= choice <= 7 else None
    except ValueError:
        return None


def main():
    pass

if __name__ == "__main__":
    main()
