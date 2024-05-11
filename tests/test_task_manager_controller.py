import os
import sys

# Get the absolute path of the parent directory of the current file (i.e., tests directory)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

import unittest
from unittest.mock import MagicMock
from implementation.task_manager_controller import TaskManagerController


class TestTaskManagerController(unittest.TestCase):
    def setUp(self):
        self.ui = MagicMock()
        self.model = MagicMock()
        self.controller = TaskManagerController(self.ui, self.model)

    def test_create_task_valid_details(self):
        self.controller.validate_task_details = MagicMock(return_value=True)
        self.controller.create_task("Task 1")
        self.model.add_task.assert_called_once_with("Task 1")
        self.ui.display_message.assert_called_once_with(
            "Task created successfully")

    def test_create_task_invalid_details(self):
        self.controller.validate_task_details = MagicMock(return_value=False)
        self.controller.create_task("Invalid Task")
        self.model.add_task.assert_not_called()
        self.ui.display_message.assert_called_once_with(
            "Invalid task details")

    def test_edit_task_success(self):
        task_mock = MagicMock()
        task_mock.edit_details = MagicMock()
        self.model.get_task_by_id = MagicMock(return_value=task_mock)
        self.controller.edit_task(1, "New Description")
        task_mock.edit_details.assert_called_once_with("New Description")
        self.ui.display_message.assert_called_once_with(
            "Task 1 edited successfully")

    def test_edit_task_not_found(self):
        self.model.get_task_by_id = MagicMock(return_value=None)
        self.controller.edit_task(1, "New Description")
        self.ui.display_message.assert_called_once_with(
            "Task 1 not found")

    def test_delete_task_success(self):
        self.model.delete_task = MagicMock(return_value=True)
        self.controller.delete_task(1)
        self.ui.display_message.assert_called_once_with(
            "Task 1 deleted successfully")

    def test_delete_task_not_found(self):
        self.model.delete_task = MagicMock(return_value=False)
        self.controller.delete_task(1)
        self.ui.display_message.assert_called_once_with(
            "Task 1 not found")


if __name__ == '__main__':
    unittest.main()
