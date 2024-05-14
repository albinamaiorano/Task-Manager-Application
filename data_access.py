from models import Task


class TaskRepository:
    def get_tasks(self):
        """Retrieve tasks from the data source."""
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
        """Save a task to the data sink."""
        if task.title:  # Only save if title is not empty
            try:
                with open("tasks.txt", "a") as file:
                    file.write(f"{task.title}: {task.description}\n")
                print("Task saved successfully.")
            except IOError as e:
                print(f"Error saving task: {e}")
        else:
            print("Error: Task title cannot be empty.")

    def delete_task(self, task):
        """Delete a task from the data source."""
        tasks = self.get_tasks()
        tasks = [t for t in tasks if t.title != task.title or t.description != task.description]
        try:
            with open("tasks.txt", "w") as file:
                for t in tasks:
                    file.write(f"{t.title}: {t.description}\n")
            print("Task deleted successfully.")
        except IOError as e:
            print(f"Error deleting task: {e}")
