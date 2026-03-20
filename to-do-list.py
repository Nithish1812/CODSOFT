import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))
    except:
        print("❌ Enter a valid number!")
        continue

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added & saved!")

    elif choice == 2:
        if not tasks:
            print("📭 No tasks available!")
        else:
            print("\n📌 Your Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == 3:
        if not tasks:
            print("❌ No tasks to delete!")
            continue

        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

        try:
            num = int(input("Enter task number: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"🗑️ Deleted: {removed}")
            else:
                print("❌ Invalid number")
        except:
            print("❌ Enter a valid number!")

    elif choice == 4:
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice")