class DataSet:
    def __init__(self, name):
        self.dataset_name = name [cite: 73]
        self.data = [] [cite: 72]

    def add_data(self, values): [cite: 75]
        self.data = values
        print(f"Data saved to {self.dataset_name}.")
