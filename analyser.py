import numpy as np

class Analyzer:
    def __init__(self, dataset_obj): [cite: 80]
        self.dataset = dataset_obj.data

    def calculate_mean(self): [cite: 82]
        return np.mean(self.dataset) if self.dataset else 0

    def find_max(self): [cite: 84]
        return np.max(self.dataset) if self.dataset else 0
