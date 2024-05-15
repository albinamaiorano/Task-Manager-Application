from models import Task

class TaskRepository:
    """A class to handle task data access operations."""

    def get_tasks(self):
        """Retrieve tasks from the data source.

        Returns:
            list: A list of Task objects representing tasks retrieved from the data source.
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
        except IOError as e:
            print(f"Error reading task file: {e}")
        return tasks

    def save_task(self, task):
        """Save a task to the data sink.

        Args:
            task (Task): The task object to be saved.

        Raises:
            ValueError: If the task title is empty.
            IOError: If there is an error saving the task to the data sink.
        """
        if not task.title:
            raise ValueError("Task title cannot be empty.")

        try:
            with open("tasks.txt", "a") as file:
                file.write(f"{task.title}: {task.description}\n")
            print("Task saved successfully.")
        except IOError as e:
            print(f"Error saving task: {e}")

    def delete_task(self, task):
        """Delete a task from the data source.

        Args:
            task (Task): The task object to be deleted.

        Raises:
            IOError: If there is an error deleting the task from the data source.
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
