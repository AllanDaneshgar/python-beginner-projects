import json
import os
from datetime import datetime

class Contact():
    def __init__(self, file_name=".contact.json"):
        self.filename = file_name
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    self.contacts = json.load(file)
                print(f"📂 Loaded {len(self.contacts)} contacts")

            except:
                print("⚠️ Could not load contacts. Starting fresh.")
                self.contacts = []
        else:
            print("📝 No contacts file found. Starting fresh.")
            self.contacts = []

    def save_contacts(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.contacts, file, indent=2)
        print("💾 Contacts saved!")

    def get_new_id(self):
        if self.contacts:
            return max(c["id"] for c in self.contacts) + 1
        return 1

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
    print("")

if __name__ == "__main__":
    main()
