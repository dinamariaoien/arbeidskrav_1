# Oppgave 5 - Miniprosjekt: aktivitetsplanlegger

class Activity:
    """Beskriver en planlagt eller fullførst aktivitet."""  # Docstring

    def __init__(self, title, category, date, estimated_minutes, status):
    # __init__ = en spesiell metode som kjøres automatisk hver gang et nytt objekt blir laget
    # Eksempel fra forelsening onsdag uke 39
        self.title = title  # self viser til dette spesifikke objektet.
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

    def mark_completed(self):
        """Endrer aktivitetstatusen til completed"""
        self.status = "Completed"





