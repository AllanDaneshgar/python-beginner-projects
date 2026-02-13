import json
import os
import re
from datetime import datetime
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class ContactManager():
    def __init__(self, file_name="contact.json"):
        self.filename = os.path.join(BASE_DIR, file_name)
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
        else:
            return 1

    def add_contact(self):
        print("\n➕ ADD NEW CONTACT")
        print("-" * 20)

        name = input("Name: ").strip()
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                print("❌ This Contact already exists!")
                return
        if not name:
            print("❌ Name cannot be empty!\n Defult Value => None")
            return


        phone = input("phone: ").strip()
        if not phone:
            print("❌ Phone cannot be empty!\n Defult Value => None")
            return
        elif len(phone) > 11:
            print("❌ The phone number cannot exceed 11 digits!\n Defult Value => 0")
            return

        email = input("email: ").strip()
        if not email:
            print("❌ email cannot be empty!\nDefault Value => None")
            return
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(regex, email):
            print("❌ invalid email!")
            return

        print("Groups: family, friends, work")
        group = input("Group: ").strip().lower()
        if group not in ["family", "friends", "work"]:
            print("⚠️ Invalid group! Using 'friends'")
            group = "friends"

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_contact = {
            "id": self.get_new_id(),
            "name": name,
            "phone": phone,
            "email": email,
            "group": group,
            "time": current_time
        }

        self.contacts.append(new_contact)
        self.save_contacts()
        print(f"✅ Contact added (ID: {new_contact['id']})")

def show_menu():
    print("\n" + "-"*30)
    print("1. ➕ Add new contact")
    print("2. 👥 View all contacts")
    print("3. 🔍 Search contacts")
    print("4. 🗑️ Delete contact")
    print("5. 📊 Show statistics")
    print("6. 🚪 Exit")

    try:
        choice = int(input("Choose (1-6): "))
        return choice if 1 <= choice <= 6 else None
    except ValueError:
        return None


def main():
    print("=" * 50)
    print("📞 WELCOME TO CONTACT MANAGER")
    print("Contacts are saved in 'contacts.json'")

    manager = ContactManager()

    while True:
        choice = show_menu()
        if choice == 1:
            manager.add_contact()

        elif choice == 6:
            print("\n👋 Goodbye!")
            print("Thank you for using Contact Manager!")
            break
        else:
            print("⚠️ Please choose 1-7")




if __name__ == "__main__":
    main()
