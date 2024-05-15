import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic import TaskService
from models import Task
from data_access import TaskRepository

class TestTaskService(unittest.TestCase):
    def setUp(self):
        self.task_service = TaskService()

    def test_add_task(self):
        print("Testing adding a task...")
        # Test adding a task with valid input
        new_task = Task(title="Test Task", description="This is a test task.")
        with patch('builtins.input', side_effect=["Test Task", "This is a test task."]):
            with patch('sys.stdout', new_callable=StringIO):
                result = self.task_service.add_task(new_task)
                print("Add Task Output:", result)
                self.assertEqual(result, "Task added successfully!")

        print("\nTesting adding a task with an empty title...")
        # Test adding a task with an empty title
        new_task_empty_title = Task(title="", description="This is an empty title task.")
        result_empty_title = self.task_service.add_task(new_task_empty_title)
        print("Add Task Output (Empty Title):", result_empty_title)
        self.assertEqual(result_empty_title, "Task title cannot be empty.")

        print("\nTesting adding a task with a long title...")
        # Test adding a task with a long title
        long_title = "a" * 101  # Assuming TASK_MAX_LENGTH is 100
        new_task_long_title = Task(title=long_title, description="This is a long title task.")
        result_long_title = self.task_service.add_task(new_task_long_title)
        print("Add Task Output (Long Title):", result_long_title)
        self.assertEqual(result_long_title, "Task title or description exceeds maximum length.")

    def test_get_all_tasks(self):
        print("\nTesting getting all tasks...")
        # Assuming some tasks exist in the data source
        expected_tasks = [Task(title="Task 1", description="Description 1"),
                          Task(title="Task 2", description="Description 2")]
        with patch.object(TaskRepository, 'get_tasks', return_value=expected_tasks):
            tasks = self.task_service.get_all_tasks()
            print("Get All Tasks Output:", tasks)
            self.assertEqual(tasks, expected_tasks)

        # Assuming no tasks exist in the data source
        print("\nTesting getting all tasks when no tasks exist...")
        with patch.object(TaskRepository, 'get_tasks', return_value=[]):
            tasks = self.task_service.get_all_tasks()
            print("Get All Tasks Output (No Tasks):", tasks)
            self.assertEqual(tasks, [])

    def test_delete_task(self):
        print("\nTesting deleting a task...")
        # Test deleting a task
        task_to_delete = Task(title="Task to delete", description="Description to delete")
        with patch.object(TaskRepository, 'delete_task') as mock_delete_task:
            result = self.task_service.delete_task(task_to_delete)
            print("Delete Task Output:", result)
            mock_delete_task.assert_called_once_with(task_to_delete)
            self.assertEqual(result, "Task deleted successfully!")


if __name__ == '__main__':
    unittest.main()
