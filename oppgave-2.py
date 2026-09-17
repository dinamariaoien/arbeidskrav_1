# Oppgave 2 Oppgave 2 – Datastrukturer og behandling av data
study_sessions = [
    {"topic":"Math", "duration_minutes":45, "status":"completed"},
    {"topic":"Science", "duration_minutes":120, "status":"planned"},
    {"topic":"Business", "duration_minutes":30, "status":"planned"},
    {"topic":"Psychology", "duration_minutes":60, "status":"completed"},
    {"topic":"Religion", "duration_minutes":45, "status":"completed"}
]

running = True

while running:
    print("\n1. Registrer en studieøkt.")
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

            except ValueError:
                print("Må være et heltall.")

        status = input("Status (planned/completed): ")

        while status != "planned" and status != "completed":
            print("Status må være planned eller completed.")
            status = input("Status (planned/completed): ")

        new_session = {
            "topic": topic,
            "duration_minutes": duration_minutes,
            "status": status
        }
        study_sessions.append(new_session)

    elif choice == "2": # Vis alle studieøkter
        for session in study_sessions:
            print(session["topic"], "-", session["duration_minutes"], "-", session["status"])

    elif choice == "3": # Vis fullførte studieøkter
        for session in study_sessions:
            if session["status"] == "completed":
                print(session["topic"], "-", session["status"])

    elif choice == "4": # Søk etter ord i temaet
        word_search = input("Søk etter tema: ")

        for session in study_sessions:
            if word_search.lower() in session["topic"].lower(): # Gjorde lignende i 1.2 
                print(session)

    elif choice == "5": # Sorter etter varighet
        def sort_duration (session):
            return session["duration_minutes"]
        study_sessions.sort(key=sort_duration, reverse=True) # Denne løsningen kom opp automatisk i programmet

        for session in study_sessions:
            print(session["topic"], "-", session["duration_minutes"])


    elif choice == "6": # Vis samlet og gjennomsnittlig varighet
        total_duration = 0

        for session in study_sessions:
            if session["status"] == "completed":
                total_duration = total_duration + session["duration_minutes"]

        average_duration = total_duration / len(study_sessions)

        print(f"Samlet varighet: {total_duration} minutter")
        print(f"Gjenomsnittlig varighet: {average_duration} minutter")

    else:
        print("Hadebra!") # Avslutt
        running = False



               







