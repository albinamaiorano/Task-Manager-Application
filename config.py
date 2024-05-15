class Config:
    """Configuration class for the Task Manager Application."""

    FILENAME = "tasks.txt"
    """str: The filename of the task data file."""

    def __init__(self):
        """Initialize the Config class."""
        pass

    def get_filename(self):
        """Get the filename of the task data file.

        Returns:
            str: The filename of the task data file.
        """
        return self.FILENAME

    def set_filename(self, filename):
        """Set the filename of the task data file.

        Args:
            filename (str): The new filename for the task data file.
        """
        self.FILENAME = filename
