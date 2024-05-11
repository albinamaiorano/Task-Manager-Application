from implementation.task import Task


class TaskManagerModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_details):
        """Add a new task."""
        task = Task(task_details)
        # Assuming Task class is defined with an id attribute
        self.tasks.append(task)

    def get_task_by_id(self, task_id):
        """Get a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task  # Return the task object if found
        return None  # Return None if task is not found

    def delete_task(self, task_id):
        """Delete a task by its ID."""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False
