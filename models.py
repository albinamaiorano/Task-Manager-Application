class Task:
    """A class representing a task.

    Attributes:
        title (str): The title of the task.
        description (str): The description of the task.

    Examples:
        >>> task = Task("Example Task", "This is an example task.")
        >>> task.title
        'Example Task'
        >>> task.description
        'This is an example task.'
    """

    def __init__(self, title: str, description: str):
        """Initialize a task with a title and description.

        Args:
            title (str): The title of the task.
            description (str): The description of the task.
        """
        self.title = title
        self.description = description
