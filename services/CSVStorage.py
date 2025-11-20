# services/CSVStorage.py
import csv
import os

class CSVStorage:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_dir = os.path.join(self.base_dir, "data")
        os.makedirs(self.data_dir, exist_ok=True)
    
    def load(self, filename):
        try:
            filepath = os.path.join(self.data_dir, filename)
            if not os.path.exists(filepath):
                return []
            
            with open(filepath, 'r', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return [row for row in reader]
        except Exception as e:
            print(f"Erreur chargement {filename}: {e}")
            return []

    def save(self, filename, fieldnames, data):
        try:
            filepath = os.path.join(self.data_dir, filename)
            file_exists = os.path.isfile(filepath)
            
            with open(filepath, 'a', newline='', encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(data)
            return True
        except Exception as e:
            print(f"Erreur sauvegarde {filename}: {e}")
            return False