import os
import sys

# Get the absolute path of the parent directory of the current file (i.e., tests directory)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the Python path
sys.path.append(parent_dir)
import unittest
from unittest.mock import patch
from io import StringIO
from implementation.user_interface import UserInterface


class TestUserInterface(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_tasks(self, mock_stdout):
        ui = UserInterface()
        tasks = ['Task 1', 'Task 2', 'Task 3']
        expected_output = "Tasks:\nTask 1\nTask 2\nTask 3\n"
        ui.display_tasks(tasks)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_edit_task(self):
        ui = UserInterface()  # Create an instance of UserInterface
        with patch('builtins.input', return_value='New Description'):
            new_description = ui.edit_task(1)  # Use ui instead of self.ui
            self.assertEqual(new_description, 'New Description')

    def test_delete_task_confirmation_yes(self):
        ui = UserInterface()  # Create an instance of UserInterface
        with patch('builtins.input', return_value='yes'):
            confirmation = ui.delete_task(1)  # Use ui instead of self.ui
            self.assertTrue(confirmation)

    def test_delete_task_confirmation_no(self):
        ui = UserInterface()  # Create an instance of UserInterface
        with patch('builtins.input', return_value='no'):
            confirmation = ui.delete_task(1)  # Use ui instead of self.ui
            self.assertFalse(confirmation)


if __name__ == '__main__':
    unittest.main()
