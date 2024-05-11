import sys
import os


# Get the absolute path to the directory containing the data_access package
data_access_dir = os.path.abspath('/Users/alba/Desktop/Task Manager Application/data_access')

# Add the data_access directory to the Python path
sys.path.append(data_access_dir)

# Now you can import the FileDataAccess class directly
from file_data_access import FileDataAccess


def main():
    # Get the absolute path of the parent directory of the current file
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Construct the absolute path to the data directory
    data_dir = os.path.join(parent_dir, 'data')

    # Path to the data file
    data_file_path = os.path.join(data_dir, 'tasks.json')

    # Instantiate FileDataAccess with the data file path
    data_access = FileDataAccess(data_file_path)

    # Read tasks from the file
    try:
        tasks = data_access.read_data()
        print("Tasks before updating:", tasks)
    except Exception as e:
        print("Error reading data:", e)
        return

    # Add a new task to the list of tasks
    new_task = {'id': 1, 'description': 'Sample Task', 'completed': False}
    tasks.append(new_task)
    print("Tasks after updating:", tasks)

    # Write updated tasks back to the file
    try:
        data_access.write_data(tasks)
    except Exception as e:
        print("Error writing data:", e)


if __name__ == "__main__":
    main()
