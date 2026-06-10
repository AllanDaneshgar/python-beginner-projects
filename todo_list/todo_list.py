"""
Todo List Manager - Python Project
Save your tasks in a JSON file
"""

import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="tasks.json"):
        """Initialize todo list with file storage"""
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file"""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Return empty list if file doesn't exist or is empty

    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    def add_task(self, title, category="personal", priority="medium"):
        """Add a new task"""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "category": category,
            "priority": priority,
            "done": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "due_date": None
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task added: {title}")
        return task

    def show_tasks(self, show_all=True):
        """Show all tasks or only pending ones"""
        print("\n" + "="*50)
        print("📋 YOUR TASKS")
        print("="*50)

        if not self.tasks:
            print("No tasks yet! Add some tasks first.")
            return

        pending_count = 0
        for task in self.tasks:
            if not task["done"] or show_all:
                status = "✅" if task["done"] else "⏳"
                priority_symbol = self.get_priority_symbol(task["priority"])

                print(f"{task['id']:3}. {status} {priority_symbol} {task['title']}")
                print(f"     📁 Category: {task['category']} | 🕐 Created: {task['created_at']}")
                if task['due_date']:
                    print(f"     📅 Due: {task['due_date']}")
                print()

                if not task["done"]:
                    pending_count += 1

        print(f"📊 Total: {len(self.tasks)} tasks | ⏳ Pending: {pending_count}")
        print("="*50)

    def get_priority_symbol(self, priority):
        """Get emoji for priority"""
        symbols = {
            "high": "🔴",
            "medium": "🟡",
            "low": "🟢"
        }
        return symbols.get(priority, "⚪")

    def mark_done(self, task_id):
        """Mark a task as done"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                self.save_tasks()
                print(f"✅ Task {task_id} marked as done!")
                return True
        print(f"❌ Task {task_id} not found!")
        return False

    def delete_task(self, task_id):
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted_task = self.tasks.pop(i)
                # Update IDs for remaining tasks
                for j in range(i, len(self.tasks)):
                    self.tasks[j]["id"] = j + 1
                self.save_tasks()
                print(f"🗑️ Task '{deleted_task['title']}' deleted!")
                return True
        print(f"❌ Task {task_id} not found!")
        return False

    def search_tasks(self, keyword):
        """Search tasks by keyword"""
        results = []
        for task in self.tasks:
            if keyword.lower() in task["title"].lower():
                results.append(task)

        print(f"\n🔍 Search results for '{keyword}':")
        if results:
            for task in results:
                status = "✅" if task["done"] else "⏳"
                print(f"  {status} {task['title']} (ID: {task['id']})")
        else:
            print("  No tasks found!")

        return results

    def get_statistics(self):
        """Show task statistics"""
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task["done"])
        pending = total - done

        categories = {}
        for task in self.tasks:
            cat = task["category"]
            categories[cat] = categories.get(cat, 0) + 1

        print("\n" + "="*50)
        print("📊 TASK STATISTICS")
        print("="*50)
        print(f"📈 Total tasks: {total}")
        print(f"✅ Completed: {done} ({done/total*100:.1f}%)" if total > 0 else "✅ Completed: 0")
        print(f"⏳ Pending: {pending} ({pending/total*100:.1f}%)" if total > 0 else "⏳ Pending: 0")

        if categories:
            print("\n📁 By category:")
            for cat, count in categories.items():
                print(f"  {cat}: {count}")

        print("="*50)

def show_menu():
    """Display main menu"""
    print("\n" + "="*40)
    print("📝 TODO LIST MANAGER")
    print("="*40)
    print("1. Add new task")
    print("2. View all tasks")
    print("3. View pending tasks")
    print("4. Mark task as done")
    print("5. Delete task")
    print("6. Search tasks")
    print("7. Statistics")
    print("8. Exit")
    print("="*40)

    try:
        choice = int(input("Choose option (1-8): "))
        if 1 <= choice <= 8:
            return choice
        else:
            print("⚠️ Please choose between 1-8")
            return None
    except ValueError:
        print("⚠️ Please enter a number!")
        return None

def get_input(prompt, default=""):
    """Get user input with optional default value"""
    if default:
        user_input = input(f"{prompt} [{default}]: ").strip()
        return user_input if user_input else default
    return input(prompt).strip()

def main():
    """Main function"""
    print("="*50)
    print("📝 WELCOME TO TODO LIST MANAGER")
    print("="*50)
    print("Your tasks are automatically saved to 'tasks.json'")

    todo = TodoList()

    while True:
        choice = show_menu()

        if choice is None:
            continue

        if choice == 1:  # Add task
            print("\n➕ ADD NEW TASK")
            print("-" * 20)
            title = get_input("Task title: ")
            if not title:
                print("❌ Task title cannot be empty!")
                continue

            category = get_input("Category (work/personal/shopping/other)", "personal")
            priority = get_input("Priority (high/medium/low)", "medium")

            todo.add_task(title, category, priority)

        elif choice == 2:  # View all tasks
            todo.show_tasks(show_all=True)

        elif choice == 3:  # View pending tasks
            todo.show_tasks(show_all=False)

        elif choice == 4:  # Mark as done
            todo.show_tasks(show_all=False)
            try:
                task_id = int(input("\nEnter task ID to mark as done: "))
                todo.mark_done(task_id)
            except ValueError:
                print("❌ Please enter a valid number!")

        elif choice == 5:  # Delete task
            todo.show_tasks(show_all=True)
            try:
                task_id = int(input("\nEnter task ID to delete: "))
                confirm = input(f"Are you sure? (y/n): ").lower()
                if confirm == 'y':
                    todo.delete_task(task_id)
                else:
                    print("❌ Deletion cancelled!")
            except ValueError:
                print("❌ Please enter a valid number!")

        elif choice == 6:  # Search
            keyword = input("\nEnter search keyword: ")
            todo.search_tasks(keyword)

        elif choice == 7:  # Statistics
            todo.get_statistics()

        elif choice == 8:  # Exit
            print("\n👋 Thank you for using Todo List!")
            print("Your tasks are saved. Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
