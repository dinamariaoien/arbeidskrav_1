# Oppgave 2 Oppgave 2 – Datastrukturer og behandling av data
study_sessions = [   # Liste med dictionaries
    {"topic":"Math", "duration_minutes":45, "status":"completed"},
    {"topic":"Science", "duration_minutes":120, "status":"planned"},
    {"topic":"Business", "duration_minutes":30, "status":"planned"},
    {"topic":"Psychology", "duration_minutes":60, "status":"completed"},
    {"topic":"Religion", "duration_minutes":45, "status":"completed"}
]

running = True  # Programmet kjøres helt til det blir fortalt at det skal slutte

while running:
    print("\n1. Registrer en studieøkt.")   # Meny
    print("2. Vis alle studieøkter")
    print("3. Vis fullførte studieøkter")
    print("4. Søk etter ord i temaet")
    print("5. Sorter etter varighet")
    print("6. Vis samlet og gjennomsnittlig varighet")
    print("7. Avslutt")

    choice = input("Velg et alternativ (1-7): ")

    if choice == "1": # Registrer en studieøkt.
        topic = input("Tema: ")

        while topic == "":
            print("Feltet kan ikke væe tomt.")
            topic = input("Tema: ")

        while True:
            try:
                duration_minutes = int(input("Hvor mange minutter varer studieøkten?: "))

                if duration_minutes > 0:
                    break
                else:
                    print("Må være et positivt tall.")

            except ValueError:  # Gir feilmelding istedenfor å kræsje
                print("Må være et heltall.")

        status = input("Status (planned/completed): ")

        while status != "planned" and status != "completed":   # != betyr "er ikke lik"
            print("Status må være planned eller completed.")
            status = input("Status (planned/completed): ")

        new_session = {
            "topic": topic,
            "duration_minutes": duration_minutes,
            "status": status
        }
        study_sessions.append(new_session)  # append legger til i listen

    # Vis alle studieøkter
    elif choice == "2":
        for session in study_sessions:
            print(session["topic"], "-", session["duration_minutes"], "-", session["status"])

    # Vis fullførte studieøkter
    elif choice == "3":
        for session in study_sessions:
            if session["status"] == "completed":
                print(session["topic"], "-", session["status"])

    # Søk etter ord i temaet
    elif choice == "4":
        word_search = input("Søk etter tema: ")

        for session in study_sessions:
            if word_search.lower() in session["topic"].lower(): # Gjorde lignende i 1.2 
                print(session)

    # Sorter etter varighet
    elif choice == "5":
        def sort_duration (session):
            return session["duration_minutes"]
        study_sessions.sort(key=sort_duration, reverse=True) # Denne løsningen kom opp automatisk i programmet

        for session in study_sessions:
            print(session["topic"], "-", session["duration_minutes"])

    # Vis samlet og gjennomsnittlig varighet
    elif choice == "6":
        total_duration = 0

        for session in study_sessions:
            if session["status"] == "completed":
                total_duration = total_duration + session["duration_minutes"]

        average_duration = total_duration / len(study_sessions)

        print(f"Samlet varighet: {total_duration} minutter")
        print(f"Gjenomsnittlig varighet: {average_duration} minutter")

    # Avslutt
    else:
        print("Hadebra!")
        running = False  # Blir fortalt at programmet skal slutte



               







