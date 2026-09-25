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


# Funksjon 1 - registrere og vise aktiviteter
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


# Funksjon 2 - søke etter tittel eller kategori
def show_activities(activities):
    """Funksjonen viser alle aktivitetene"""
    if len(activities) == 0:  # len() - viser hvis ingen aktiviteter hadde vært registrert
        print("Ingen registrerte")
    else:
        for activity in activities:
            print(f"Tittel: {activity.title}, Kategori: {activity.category}, Dato: {activity.date}, Estimert tid: {activity.estimated_minutes}, Status: {activity.status}")


# Funksjon 3 - filtrere etter status
def search_title_category(activities):
    search = input("Søk etter tittel eller kategori:")

    while search == "" or search == " ":
        print("Søkefeltet kan ikke være tomt.")
        search = input("Søk etter tittel eller kategori:")

    for activity in activities:
        if search.lower() in activity.title.lower() or search.lower() in activity.category.lower():
            print(f"Tittel: {activity.title}, Kategori: {activity.category}, Dato: {activity.date}, Estimert tid: {activity.estimated_minutes}, Status: {activity.status}")


# Sortere etter dato eller varighet.
# Funksjon 4 - dato
def get_date(activity):   # Funksjon til menyvalg 5, henter ut datoene så .sort() kan gjøre jobben sin
    return datetime.strptime(activity.date, "%d.%m.%Y")  # Kovnerterer tekst til en datoverdi

# Funksjon 5 - estimerte minutter
def get_duration(activity):  # Funksjon til menyvalg 5
    return activity.estimated_minutes


# Lagre aktiviteter til fil og lese dem inn igjen.
# Funksjon 6 - lagrer aktivitetene i en fil
def save_activities(activities, filename):
    with open(filename, "w", encoding="utf-8") as file:  # w - write, gjorde lignende tidligere i oppg 4.
        for activity in activities:
            file.write(
                f"{activity.title},{activity.category},{activity.date},"
                f"{activity.estimated_minutes},{activity.status}\n"
            )

# Funksjon 7 - leser aktivitetene
def read_activities(filename):
    activities = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                title, category, date, estimated_minutes, status = line.strip().split(",")  # srip fjerner tomrom og linjeskift, split deler teksten opp i flere deler

                activity = Activity(
                    title,
                    category,
                    date,
                    int(estimated_minutes),
                    status
                )

                activities.append(activity)

    except FileNotFoundError:
        print("Filen ble ikke funnet")

    return activities


# Leser inn lagrede aktiviteter når programmet starter, før menyen vises
activities = read_activities("activities.txt")


# Videre til meny
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
            status = input("Velg status planned/completed: ")

        for activity in activities:
            if activity.status == status:
                print(f"Tittel: {activity.title}, Kategori: {activity.category}, Dato: {activity.date}, Estimert tid: {activity.estimated_minutes}, Status: {activity.status}")


    # Sortere etter dato eller varighet.
    elif choice == "5":
        print("Hva vil du sortere etter?\n1. Dato\n2. Varighet")

        sort_choice = input("Velg 1 eller 2:")

        while sort_choice != "1" and sort_choice != "2":
            print("Ugyldig valg, prøv igjen!")
            sort_choice = input("Velg 1 eller 2:")

        if sort_choice == "1":
                activities.sort(key=get_date)   # Key forteller sort() hvilken verdi den skal bruke
                show_activities(activities)

        elif sort_choice == "2":
                activities.sort(key=get_duration)
                show_activities(activities)


    # Markere en aktivitet som fullført
    elif choice == "6":
        title = input("Skriv tittelen på aktiviteten som er fullført: ")

        while title == "" or title == " ":
            print("Tittel kan ikke være tom.")
            title = input("Skriv tittelen på aktiviteten som er fullført: ")

        for activity in activities:
            if activity.title.lower() == title.lower():  # lower gjør teksten til små bokstaver for å sammenligne titlene
                activity.mark_completed()   # Metoden i Activity klassen
                print("Aktiviteten er markert som fullført.")


    # Vise antall aktiviteter, samlet estimert tid og antall fullførte.
    elif choice == "7":
        # Antall aktiviteter
        number_of_activities = len(activities)

        # Regner ut samlet tid
        total_minutes = 0
        for activity in activities:
            total_minutes += activity.estimated_minutes   # += er en kortere måte å skrive : total = xx + yy (eksempel)

        # Fullførte aktiviteter
        completed_count = 0
        for activity in activities:    # Gjort lignende tidligeere i arbeidskravet + løsningen kom opp automatisk
            if activity.status == "completed":
                completed_count += 1

        print(f"Antall aktiviteter: {number_of_activities}")
        print(f"Samlet estimert tid: {total_minutes}")
        print(f"Antall fullførte aktiviteter: {completed_count}")


    # Lagre aktiviteter til fil og lese dem inn igjen.
    elif choice == "8":
        save_activities(activities, "activities.txt")
        print("Aktivitetene er lagret.")

    # Avslutt
    elif choice == "9":
        print("Hadebra!")
        running = False

    else:
        print("Ugyldig, vennligst velg 1-9")   # Får bruker til å måtte velge mellom 1 og 9, så programmet ikke slutter selv om man skriver 10.




