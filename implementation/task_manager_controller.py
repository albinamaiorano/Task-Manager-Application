from .task_manager_model import TaskManagerModel


class TaskManagerController:
    def __init__(self, ui, model=None):
        self.ui = ui
        self.model = model or TaskManagerModel()

    def create_task(self, task_details):
        """Create a new task."""
        if self.validate_task_details(task_details):
            self.model.add_task(task_details)
            self.ui.display_message("Task created successfully")
        else:
            self.ui.display_message("Invalid task details")

    def validate_task_details(self, task_details):
        """Validate task details."""
        # Placeholder for validation logic
        return True

    def edit_task(self, task_id, new_description):
        """Edit a task."""
        task = self.model.get_task_by_id(task_id)
        if task:
            task.edit_details(new_description)
            self.ui.display_message(
                f"Task {task_id} edited successfully")
        else:
            self.ui.display_message(
                f"Task {task_id} not found")

    def delete_task(self, task_id):
        """Delete a task."""
        if self.model.delete_task(task_id):
            self.ui.display_message(
                f"Task {task_id} deleted successfully")
        else:
            self.ui.display_message(
                f"Task {task_id} not found")
