class Task:
    _id_counter = 1  # Initialize ID counter

    def __init__(self, details):
        self.id = Task._id_counter  # Assign unique ID to each task
        Task._id_counter += 1  # Increment ID counter for the next task
        self.details = details
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def edit_details(self, new_details):
        """Edit the details of the task."""
        self.details = new_details

    def __str__(self):
        """String representation of the task."""
        status = "(Completed)" if self.completed else ""
        # Remove trailing spaces
        return f"Task {self.id}: {self.details} {status}".strip()
