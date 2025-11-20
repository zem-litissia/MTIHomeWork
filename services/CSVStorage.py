# services/CSVStorage.py
import csv
import os

class CSVStorage:
    """Classe utilitaire pour lire et écrire des CSV"""

    @staticmethod
    def load(filename):
        try:
            print(f"Tentative de chargement de: {filename}")
            if not os.path.exists(filename):
                print(f"Fichier {filename} non trouvé, retourne liste vide")
                return []
            
            with open(filename, 'r', newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                data = [row for row in reader]
                print(f"Chargement réussi: {len(data)} lignes depuis {filename}")
                return data
        except Exception as e:
            print(f"ERREUR lors du chargement de {filename}: {e}")
            return []

    @staticmethod
    def save(filename, fieldnames, data):
        try:
            print(f"Tentative de sauvegarde dans: {filename}")
            print(f"Données à sauvegarder: {data}")
            
            # Vérifier si le fichier existe
            file_exists = os.path.isfile(filename)
            print(f"Fichier existe: {file_exists}")
            
            with open(filename, 'a', newline='', encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                # Écrire l'en-tête si le fichier n'existe pas
                if not file_exists:
                    print("Écriture de l'en-tête...")
                    writer.writeheader()
                
                print("Écriture des données...")
                writer.writerow(data)
            
            print(f"SAUVEGARDE RÉUSSIE dans {filename}")
            return True
        except Exception as e:
            print(f"ERREUR lors de la sauvegarde dans {filename}: {e}")
            return False