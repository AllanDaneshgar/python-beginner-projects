import json
import os
import re
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class ContactManager:
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
            if any(
                contact["name"].lower() == name.lower() for contact in self.contacts
            ):
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
            email = input("Email (optional): ").strip()
            if email:
                regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
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

        current_time = datetime.now().isoformat()

        new_contact = {
            "id": self.get_new_id(),
            "name": name,
            "phone": phone,
            "email": email,
            "group": group,
            "created_at": current_time,
            "updated_at": current_time,
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
        sorted_contacts = sorted(self.contacts, key=lambda x: x["name"])
        for contact in sorted_contacts:
            print(f"ID: {contact['id']}")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Group: {contact['group']}")
            print(f"Created: {contact['created_at']}")
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
            print(f"Created: {contact['created_at']}")
            print("-" * 20)

    def edit_contact(self):
        print("\n✏️ EDIT CONTACT")
        self.show_all_contacts()
        try:
            contact_id = int(input("\nEnter contact ID to edit: "))
        except ValueError:
            print("❌ Please enter a number!")
            return

        for contact in self.contacts:
            if contact["id"] == contact_id:
                print(f"\nEditing {contact['name']} (ID: {contact_id})")
                print("Leave blank to keep current value.")

                new_name = input(f"Name [{contact['name']}]: ").strip()
                if new_name:
                    if any(c["name"].lower() == new_name.lower() for c in self.contacts if c["id"] != contact_id):
                        print("❌ This name already exists!")
                        return
                    contact["name"] = new_name

                new_phone = input(f"Phone [{contact['phone']}]: ").strip()
                if new_phone:
                    if not new_phone.isdigit():
                        print("❌ Phone must contain only digits!")
                        return
                    if len(new_phone) > 11:
                        print("❌ Phone cannot exceed 11 digits!")
                        return
                    contact["phone"] = new_phone

                new_email = input(f"Email [{contact['email']}]: ").strip()
                if new_email:
                    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                    if not re.fullmatch(regex, new_email):
                        print("❌ Invalid email!")
                        return
                    contact["email"] = new_email

                new_group = input(f"Group (family/friends/work) [{contact['group']}]: ").strip().lower()
                if new_group:
                    if new_group not in ["family", "friends", "work"]:
                        print("❌ Invalid group!")
                        return
                    contact["group"] = new_group

                contact["updated_at"] = datetime.now().isoformat()
                self.save_contacts()
                print("✅ Contact updated!")
                return

        print(f"❌ Contact with ID {contact_id} not found!")

    def delete_contact(self):
        print("\n🗑️ DELETE CONTACT")
        self.show_all_contacts()
        try:
            contact_id = int(input("\nEnter contact ID to delete: "))
        except ValueError:
            print("❌ Please enter a number!")
            return

        for i, contact in enumerate(self.contacts):
            if contact["id"] == contact_id:
                confirm = input(f"Delete {contact['name']}? (y/n): ").lower()
                if confirm == "y":
                    del self.contacts[i]
                    self.save_contacts()
                    print("✅ Contact deleted!")
                else:
                    print("❌ Deletion cancelled!")
                return
        print(f"❌ Contact with ID {contact_id} not found!")

    def show_statistics(self):
        print("\n📊 STATISTICS")
        print("=" * 40)

        total = len(self.contacts)
        print(f"Total contacts: {total}")

        if total == 0:
            return

        groups = {}
        for contact in self.contacts:
            group = contact["group"]
            groups[group] = groups.get(group, 0) + 1

        print("\n📁 By group:")
        for group, count in groups.items():
            print(f"  {group}: {count}")


def show_menu():
    print("\n" + "-" * 30)
    print("1. ➕ Add new contact")
    print("2. 👥 View all contacts")
    print("3. 🔍 Search contacts")
    print("4. ✏️ Edit contact")
    print("5. 🗑️ Delete contact")
    print("6. 📊 Show statistics")
    print("7. 🚪 Exit")
    try:
        choice = int(input("Choose (1-7): "))
        return choice if 1 <= choice <= 7 else None
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
        elif choice == 3:
            manager.search_contact()
        elif choice == 4:
            manager.edit_contact()
        elif choice == 5:
            manager.delete_contact()
        elif choice == 6:
            manager.show_statistics()
        elif choice == 7:
            print("\n👋 Goodbye!")
            print("Thank you for using Contact Manager!")
            break
        else:
            print("⚠️ Please choose a valid option (1-7)")


if __name__ == "__main__":
    main()
