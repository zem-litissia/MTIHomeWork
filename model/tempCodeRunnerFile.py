from club import Club
if __name__ == "__main__":
    sci_club = Club("Bouira Scientific Club")
    sci_club.load_members("members.csv")
    sci_club.load_events("events.csv")
    sci_club.load_trainings("trainings.csv")
    sci_club.load_subscriptions("subscriptions.csv")

    sci_club.summary()
    sci_club.generate_html()
