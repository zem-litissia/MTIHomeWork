import csv
import os
import threading

class CSVStorage:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
            return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_dir = os.path.join(self.base_dir, "data")
        os.makedirs(self.data_dir, exist_ok=True)
        self._initialized = True
    
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
