class Task:
    def __init__(self, name, priority, due_date):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        """Mark task as completed"""
        self.completed = True

    def to_file(self):
        """Convert task to file format"""
        return f"{self.name}|{self.priority}|{self.due_date}|{self.completed}"

    @staticmethod
    def from_file(line):
        """Create task from file line"""
        name, priority, due_date, completed = line.strip().split("|")

        task = Task(name, priority, due_date)

        if completed == "True":
            task.completed = True
        else:
            task.completed = False

        return task


# ---------------- FUNCTIONS , these are the functions that i used for this task manager.
def add_task(task_list):
    """Add a new task"""

    name = input("Enter task name: ")

    # Input validation (complex technique)
    while True:
        priority = input("Enter priority (High/Medium/Low): ")

        if priority in ["High", "Medium", "Low"]:
            break
        else:
            print("Invalid priority. Try again.")

    due_date = input("Enter due date: ")

    new_task = Task(name, priority, due_date)

    task_list.append(new_task)

    print("Task added successfully")


def show_tasks(task_list):
    """Display all tasks"""

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
    """Save tasks to file"""

    file = open("tasks.txt", "w")

    for task in task_list:
        file.write(task.to_file() + "\n")

    file.close()

    print("Tasks saved")


def load_tasks():
    """Load tasks from file"""

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
    """Mark task complete"""

    show_tasks(task_list)

    if len(task_list) == 0:
        return

    try:
        choice = int(input("Enter task number: "))

        if 1 <= choice <= len(task_list):

            task_list[choice-1].mark_completed()

            print("Task completed")

        else:
            print("Invalid number")

    except ValueError:
        print("Enter a number only")


# ---------------- MAIN MENU ----------------

def main():

    task_list = load_tasks()

    while True:

        print("\nTask Manager")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("4. Save tasks")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task(task_list)

        elif choice == "2":
            show_tasks(task_list)

        elif choice == "3":
            complete_task(task_list)

        elif choice == "4":
            save_tasks(task_list)

        elif choice == "5":
            save_tasks(task_list)
            print("Goodbye")
            break

        else:
            print("Invalid choice")


# Run program
main()