from data_access import TaskRepository
from constants import TASK_MAX_LENGTH


class TaskService:
    def __init__(self):
        """Initialize the Task Service with a Task Repository."""
        self.task_repository = TaskRepository()

    def get_all_tasks(self):
        """Get all tasks from the data source."""
        return self.task_repository.get_tasks()

    def add_task(self, task):
        """Add a new task to the data source."""
        if not task.title:
            return "Task title cannot be empty."

        if len(task.title) > TASK_MAX_LENGTH or len(task.description) > TASK_MAX_LENGTH:
            return "Task title or description exceeds maximum length."

        self.task_repository.save_task(task)
        return "Task added successfully!"

    def delete_task(self, task):
        """Delete a task from the data source."""
        self.task_repository.delete_task(task)
        return "Task deleted successfully!"
