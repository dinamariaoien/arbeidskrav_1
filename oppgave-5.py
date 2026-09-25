# Oppgave 5 - Miniprosjekt: aktivitetsplanlegger
from datetime import datetime

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


# Liste med aktiviteter
activities = [
    Activity ("Teams møte", "Jobb", "26.09.2026", 60, "planned"),
    Activity("Handle", "Personlig", "24.09.2026", 45, "completed"),
    Activity("Lese kapittel 5", "Skole", "29.09.2026", 55, "planned"),
    Activity("Levere arbeidskrav", "Skole", "22.09.2026", 15, "completed"),
]

# Funksjon 1
def add_activities(activities):
    """Legger til aktivitetet, som kan brukes senere i programmet"""
    # Tittel
    while True:
        title = input("Skriv inn tittel på aktiviteten:")

        if title == "" or title == " ":  # Passer på at programmet ikke kræsjer dersom feltet er tomt, eller mellomrom
            print("Tittel kan ikke være tom")
        else:
            break

    # Kategori
    while True:
        category = input("Skriv inn kategorien: ")

        if category == "" or category == " ":
            print("Kategori kan ikke være tom")
        else:
            break

    # Dato
    while True:
        date = input("Skriv inn dato: ")

        if date == "" or date == " ":
            print("Dato kan ikke være tom")
        else:
            break

    # Minutter
    while True:
        try:
            estimated_minutes = int(input("Hvor mange minutter vil aktiviteten vare?: "))

            if estimated_minutes < 0:
                print("Varigheten må være et positivt tall. ")
            else:
                break

        except ValueError:
            print("Varigheten må være et heltall")

    activity = Activity(title, category, date, estimated_minutes, "planned")
    activities.append(activity)  # .append for å legge til aktiviteten i lista
    print("Aktivitet registrert!")


# Funksjon 2
def show_activities(activities):
    """Funksjonen viser alle aktivitetene"""
    if len(activities) == 0:  # len() - viser hvis ingen aktiviteter hadde vært registrert, med det er allerede registrerte aktiviteter son jeg har lagt i en liste, så vet ikke om det er nødvendig?
        print("Ingen registrerte")
    else:
        for activity in activities:
            print(activity.title, activity.category, activity.date, activity.estimated_minutes)


# Funksjon 3
def search_title_category(activities):
    search = input("Søk etter tittel eller kategori:")

    while search == "" or search == " ":
        print("Søkefeltet kan ikke være tomt.")
        search = input("Søk etter tittel eller kategori:")

    for activity in activities:
        if search in activity.title or search in activity.category:
            print(activity.title, activity.category, activity.date, activity.estimated_minutes, activity.status)


#Funksjon 4
def get_date(activity):   # Funksjon til menyvalg 5, henter ut varigheten så .sort() kan gjøre jobben sin
    return datetime.strptime(activity.date, "%d.%m.%Y")

# Funksjon 5
def get_duration(activity):  # Funksjon til menyvalg 5
    return activity.estimated_minutes



running = True

while running:   # Gjorde lignende meny i oppgave 2
    print("\n1. Registrer aktivitet")
    print("2. Vis alle aktiviteter")
    print("3. Søke etter tittel eller kategori")
    print("4. Filtrer etter status")
    print("5. Sorter etter dato eller varighet")
    print("6. Markere en aktivitet som fullført")
    print("7. Vis antall aktiviteter, samlet estimert tid og antall fullførte")
    print("8. Lagre aktiviteter til fil og lese dem inn igjen")
    print("9. Avslutt")

    choice = input("Velg et alternativ (1-9): ")


    # Registrer aktivitet
    if choice == "1":
        add_activities(activities)


    # Vis alle aktiviteter
    elif choice == "2":
        show_activities(activities)


    # Søke etter tittel eller kategori
    elif choice == "3":
        search_title_category(activities)


    # Filtrer etter status
    elif choice == "4":
        status = input("Velg status (planned/completed: ")

        while status != "planned" and status != "completed":  # != betyr : er ikke lik
            print("Ugyldig status")
            status = input("Velg status (planned/completed): ")

        for activity in activities:
            if activity.status == status:
                print(activity.title, activity.category, activity.date, activity.estimated_minutes, activity.status)


    # Sortere etter dato eller varighet.
    elif choice == "5":
        print("Hva vil du sortere etter?\n1. Dato\n2. Varighet")

        sort_choice = input("Velg 1 eller 2:")

        while sort_choice != "1" and sort_choice != "2":
            print("Ugyldig valg, prøv igjen!")
            sort_choice = input("Velg 1 eller 2:")

        if sort_choice == "1":
                activities.sort(key=get_date)
                show_activities(activities)

        elif sort_choice == "2":
                activities.sort(key=get_duration)
                show_activities(activities)




