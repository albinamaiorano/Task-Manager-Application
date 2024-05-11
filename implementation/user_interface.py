class UserInterface:
    def display_tasks(self, tasks):
        """Display tasks to the user."""
        print("Tasks:")
        for task in tasks:
            print(task)

    def get_user_input(self, prompt):
        """Get user input."""
        return input(prompt)

    def display_message(self, message):
        """Display a message to the user."""
        print(message)

    def get_task_details_from_user(self):
        """Get task details from the user."""
        task_details = {}
        task_details['description'] = self.get_user_input(
            "Enter task description: ")
        task_details['priority'] = self.get_user_input(
            "Enter task priority: ")
        # Add more details as needed
        return task_details

    def get_task_to_edit(self):
        """Get the task to edit from the user."""
        task_id = self.get_user_input(
            "Enter the ID of the task to edit: ")
        # Validate task ID and return it
        return task_id

    def get_task_to_delete(self):
        """Get the task to delete from the user."""
        task_id = self.get_user_input(
            "Enter the ID of the task to delete: ")
        # Validate task ID and return it
        return task_id

    def edit_task(self, task_id):
        """Edit a task."""
        return self.get_user_input(
            f"Enter the new description for task {task_id}: ")

    def delete_task(self, task_id):
        """Delete a task."""
        confirmation = self.get_user_input(
            f"Are you sure you want to delete task {task_id}? (yes/no): ")
        return confirmation.lower() == 'yes'
