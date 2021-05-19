import pandas as pd

class Table:
    def __init__(self):
        self.pd = pd
    
    def display_CSV(self,csv_path):
        data = self.pd.read_csv(csv_path)
        print(data)