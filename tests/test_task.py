import os
import sys

# Get the absolute path of the parent directory of the current file (i.e., tests directory)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the Python path
sys.path.append(parent_dir)
import unittest
from implementation.task import Task


class TestTask(unittest.TestCase):
    def setUp(self):
        Task._id_counter = 1  # Reset _id_counter before each test case
        self.task = Task("Sample Task")

    def test_task_creation(self):
        self.assertEqual(self.task.details, "Sample Task")
        self.assertFalse(self.task.completed)

    def test_mark_completed(self):
        self.task.mark_completed()
        self.assertTrue(self.task.completed)

    def test_edit_details(self):
        new_details = "Updated Task"
        self.task.edit_details(new_details)
        self.assertEqual(self.task.details, new_details)

    def test_task_str_representation(self):
        expected_str = "Task 1: Sample Task"
        self.assertEqual(str(self.task), expected_str)

    def test_str_representation_completed_task(self):
        self.task.mark_completed()
        expected_str = "Task 1: Sample Task (Completed)"
        self.assertEqual(str(self.task), expected_str)


if __name__ == '__main__':
    unittest.main()
