import os
import sys

# Get the absolute path of the parent directory of the current file (i.e., tests directory)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the Python path
sys.path.append(parent_dir)
import unittest
from implementation.task_manager_model import TaskManagerModel


class TestTaskManagerModel(unittest.TestCase):
    def setUp(self):
        # Initialize a TaskManagerModel instance for each test case
        self.model = TaskManagerModel()

    def test_add_task(self):
        # Test adding a task to the TaskManagerModel
        initial_task_count = len(self.model.tasks)
        task_details = {'description': 'Sample Task', 'priority': 'High'}
        self.model.add_task(task_details)
        self.assertEqual(len(self.model.tasks), initial_task_count + 1)

    def test_get_task_by_id(self):
        # Test retrieving a task by its ID
        task_details = {'description': 'Sample Task', 'priority': 'High'}
        self.model.add_task(task_details)
        added_task = self.model.tasks[0]
        retrieved_task = self.model.get_task_by_id(added_task.id)
        self.assertEqual(retrieved_task, added_task)

    def test_delete_task(self):
        # Test deleting a task from the TaskManagerModel
        task_details = {'description': 'Sample Task', 'priority': 'High'}
        self.model.add_task(task_details)
        added_task = self.model.tasks[0]
        initial_task_count = len(self.model.tasks)
        self.assertTrue(self.model.delete_task(added_task.id))
        self.assertEqual(len(self.model.tasks), initial_task_count - 1)


if __name__ == '__main__':
    unittest.main()
