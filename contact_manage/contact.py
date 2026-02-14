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
            except Exception as e:
                print(f"⚠️ Could not load contacts: {e}. Starting fresh.")
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

        while True:
            name = input("Name: ").strip()
            if not name:
                print("❌ Name cannot be empty!")
                continue
            if any(contact["name"].lower() == name.lower() for contact in self.contacts):
                print("❌ This Contact already exists!")
                continue
            break

        while True:
            phone = input("Phone: ").strip()
            if not phone:
                print("❌ Phone cannot be empty!")
                continue
            if not phone.isdigit():
                print("❌ Phone must contain only digits!")
                continue
            if len(phone) > 11:
                print("❌ The phone number cannot exceed 11 digits!")
                continue
            break

        while True:
            email = input("Email: ").strip()
            if not email:
                print("❌ Email cannot be empty!")
                continue
            regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.fullmatch(regex, email):
                print("❌ Invalid email!")
                continue
            break

        while True:
            print("Groups: family, friends, work")
            group = input("Group: ").strip().lower()
            if group not in ["family", "friends", "work"]:
                print("⚠️ Invalid group! Please enter again.")
                continue
            break

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

    def show_all_contacts(self):
        print("\n👥 ALL CONTACTS")
        print("=" * 40)
        if not self.contacts:
            print("No contacts yet!")
            return
        for contact in self.contacts:
            print(f"ID: {contact['id']}")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Group: {contact['group']}")
            print(f"Time: {contact['time']}")
            print("-" * 20)

    def search_contact(self):
        print("\n🔍 SEARCH CONTACTS")
        keyword = input("Search Name: ").strip().lower()
        if not keyword:
            print("❌ Please enter a search term!")
            return
        results = []
        for c in self.contacts:
            if keyword in c["name"].lower():
                results.append(c)

        if not results:
            print("No contacts found!")
            return

        for contact in results:
            print(f"ID: {contact['id']}")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Group: {contact['group']}")
            print(f"Time: {contact['time']}")
            print("-" * 20)

    def delete_contact(self):
        print("\n🗑️ DELETE CONTACT")
        


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
    print("Contacts are saved in 'contact.json'")
    manager = ContactManager()
    while True:
        choice = show_menu()
        if choice == 1:
            manager.add_contact()
        elif choice == 2:
            manager.show_all_contacts()
        elif choice == 6:
            print("\n👋 Goodbye!")
            print("Thank you for using Contact Manager!")
            break
        else:
            print("⚠️ Please choose a valid option (1-6)")

if __name__ == "__main__":
    main()
