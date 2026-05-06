class Task:
    #// Each class will have a due date, priority, Name and cetria
    def __init__(self, name, priority, due_date):
        self.name = name  #// This stores the tasks name
        self.priority = priority #// this stores the level of how important your work, homework, things are. EG, High, Medium, Low
        self.due_date = due_date #// This stores the due date
        self.completed = False #// this is efault which isn't completed. 

    def mark_completed(self):
        self.completed = True
        #//After this is goign to change the Status to now completed

    def to_file(self):
        return f"{self.name}|{self.priority}|{self.due_date}|{self.completed}"

   
    def from_file(line):
        name, priority, due_date, completed = line.strip().split("|")

        task = Task(name, priority, due_date)
        task.completed = True if completed == "True" else False

        return task


#// These are the functions that will make the program run

def add_task(task_list):
    name = input("Enter task name: ")

    while True:
        priority = input("Enter priority (High/Medium/Low): ")
        if priority in ["High", "Medium", "Low"]:
            break
        else:
            print("Invalid priority. Try again.")

    due_date = input("Enter due date: ")

    task_list.append(Task(name, priority, due_date))
    print("Task added successfully")


def show_tasks(task_list):
    if len(task_list) == 0:
        print("No tasks found")
        return

    count = 1

    for task in task_list:
        status = "Completed" if task.completed else "Not completed"

        print(f"{count}. {task.name}")
        print(f"   Priority: {task.priority}")
        print(f"   Due date: {task.due_date}")
        print(f"   Status: {status}")

        count += 1


def save_tasks(task_list):
    file = open("tasks.txt", "w")

    for task in task_list:
        file.write(task.to_file() + "\n")

    file.close()
    print("Tasks saved")


def load_tasks():
    task_list = []

    try:
        file = open("tasks.txt", "r")

        for line in file:
            task_list.append(Task.from_file(line))

        file.close()

    except FileNotFoundError:
        print("No previous tasks found")

    return task_list


def complete_task(task_list):
    show_tasks(task_list)

    if len(task_list) == 0:
        return

    try:
        choice = int(input("Enter task number: "))

        if 1 <= choice <= len(task_list):
            task_list[choice - 1].mark_completed()
            print("Task completed")
        else:
            print("Invalid number")

    except ValueError:
        print("Enter a number only")


def delete_task(task_list):
    show_tasks(task_list)

    if len(task_list) == 0:
        return

    try:
        choice = int(input("Enter task number to delete: "))

        if 1 <= choice <= len(task_list):
            removed = task_list.pop(choice - 1)
            print(f"{removed.name} deleted successfully")
        else:
            print("Invalid number")

    except ValueError:
        print("Enter a number only")


#// This is the Main menu

def main():

    task_list = load_tasks()

    while True:

        print("\nTask Manager")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("4. Save tasks")
        print("5. Exit")
        print("6. Delete task")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_task(task_list)

        elif choice == "2":
            show_tasks(task_list)

        elif choice == "3":
            complete_task(task_list)

        elif choice == "4":
            save_tasks(task_list)

        elif choice == "6":
            delete_task(task_list)

        elif choice == "5":
            save_tasks(task_list)
            print("Goodbye")
            break

        else:
            print("Invalid choice")


#// this now runs the program

main()