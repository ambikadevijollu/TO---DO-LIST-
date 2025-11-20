# To - Do List
def show_title():
    print("\n=======YOUR PERSONAL TASK MANAGER=======")

def display_menu():
    print("\nChoose an option:")
    print(" A - Add a new task ")
    print(" L - List all tasks ")
    print(" R - Remove a task")
    print(" Q  - Quit ")

def add_task(task_box):
    new_task = input("Enter the task to add:")
    task_box.append(new_task)
    print(f"Task added: '{new_task}'")

def list_task(task_box):
    if not task_box:
       print("No tasks found yet!")
       return
    print("\nYour Tasks:")
    for index, job in enumerate(task_box, start=1):
        print(f" {index}. {job}")

def remove_task(task_box):
    list_task(task_box)
    if not task_box:
        return
    try:
        number = int(input("Enter task number to delete:"))
        removed = task_box.pop(number - 1)
        print(f"Removed task: '{removed}'")
    except(ValueError , IndexError):
        print("Invalid choice! Try again.")
def main():
    tasks_container = []
    show_title()

    while True:
        display_menu()
        choice = input("Your option: ").strip().upper()

        if choice == "A":
            add_task(tasks_container)
        elif choice == "L":
            list_task(tasks_container)
        elif choice == "R":
            remove_task(tasks_container)
        elif choice == "Q":
            print("Exiting program...Goodbye!")
            break
        else:
            print("Invalid option! Please choose again.")

if __name__ == "__main__":
    main()