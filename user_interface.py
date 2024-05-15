from models import Task

class TaskRepository:
    def get_tasks(self):
        """Retrieve tasks from the data source.

        Returns:
            list: A list of Task objects representing the retrieved tasks.
        
        Raises:
            FileNotFoundError: If the task file is not found.
            IOError: If there is an error reading the task file.
        """
        tasks = []
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(": ")
                    if len(parts) == 2:
                        title, description = parts
                        tasks.append(Task(title.strip(), description.strip()))
        except FileNotFoundError:
            print("Error: Task file not found.")
            raise
        except IOError as e:
            print(f"Error reading task file: {e}")
            raise
        return tasks

    def save_task(self, task):
        """Save a task to the data sink.

        Args:
            task (Task): The Task object to save.

        Raises:
            IOError: If there is an error saving the task to the file.
        """
        if task.title:  # Only save if title is not empty
            try:
                with open("tasks.txt", "a") as file:
                    file.write(f"{task.title}: {task.description}\n")
                print("Task saved successfully.")
            except IOError as e:
                print(f"Error saving task: {e}")
                raise
        else:
            print("Error: Task title cannot be empty.")

    def delete_task(self, task):
        """Delete a task from the data source.

        Args:
            task (Task): The Task object to delete.

        Raises:
            IOError: If there is an error deleting the task from the file.
        """
        tasks = self.get_tasks()
        tasks = [t for t in tasks if t.title != task.title or t.description != task.description]
        try:
            with open("tasks.txt", "w") as file:
                for t in tasks:
                    file.write(f"{t.title}: {t.description}\n")
            print("Task deleted successfully.")
        except IOError as e:
            print(f"Error deleting task: {e}")
            raise

class UserInterface:
    def __init__(self):
        """Initialize the UserInterface object."""
        self.task_repo = TaskRepository()

    def start_application(self):
        """Start the task manager application.

        This method displays a menu to the user and handles user interactions
        based on the selected options.

        """
        print("Welcome to Task Manager Application!")

        while True:
            print("\nChoose an option:")
            print("1. Add a task")
            print("2. View all tasks")
            print("3. Delete a task")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_all_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                print("Exiting Task Manager Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_task(self):
        """Add a new task.

        This method prompts the user to enter a new task title and description,
        creates a Task object with the provided information, and saves the task
        using the TaskRepository.

        """
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        new_task = Task(title=title, description=description)
        self.task_repo.save_task(new_task)
        print("Task added successfully.")

    def view_all_tasks(self):
        """View all tasks.

        This method retrieves all tasks from the TaskRepository and displays
        them to the user.

        """
        tasks = self.task_repo.get_tasks()
        if tasks:
            print("\nAll Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. Title: {task.title}, Description: {task.description}")
        else:
            print("No tasks found.")

    def delete_task(self):
        """Delete a task.

        This method prompts the user to enter the title and description of
        the task to delete, creates a Task object with the provided information,
        and deletes the task using the TaskRepository.

        """
        title = input("Enter the title of the task to delete: ")
        description = input("Enter the description of the task to delete: ")
        task_to_delete = Task(title=title, description=description)
        self.task_repo.delete_task(task_to_delete)
