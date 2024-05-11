import json  # Add this line to import the json module


class FileDataAccess:
    def __init__(self, data_file):
        self.data_file = data_file

    def read_data(self):
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            return data
        except json.JSONDecodeError:
            return []

    def write_data(self, data):
        with open(self.data_file, 'w') as f:
            json.dump(data, f)
