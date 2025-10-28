from club import Club
from training import TrainingSession

if __name__ == "__main__":
    # --- Créer le club scientifique ---
    sci_club = Club("Bouira Scientific Club")

    # --- Charger les données CSV ---
    sci_club.load_members("members.csv")
    sci_club.load_events("events.csv")
    sci_club.load_subscriptions("subscriptions.csv")

    # --- Créer quelques trainings manuellement (pas de fichier trainings.csv) ---
    t1 = TrainingSession("AI Workshop", "Ali Mebarki", "2024-11-10")
    t2 = TrainingSession("Cybersecurity Basics", "Omar Yacine", "2024-12-05")

    sci_club.trainings.append(t1)
    sci_club.trainings.append(t2)

    # Ajouter quelques participants à titre d’exemple
    if len(sci_club.members) >= 3:
        t1.add_participant(sci_club.members[0])
        t1.add_participant(sci_club.members[1])
        t2.add_participant(sci_club.members[2])

    # --- Afficher un résumé ---
    sci_club.summary()

    # --- Générer le tableau de bord HTML ---
    sci_club.generate_html()
