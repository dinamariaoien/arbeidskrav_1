# Oppgave 1.1 - Beregn tidsbruk
def oppgave1_1 ():
    while True:
        try:
            study_sessions = int(input("Antall studieøkter:"))
            minutes_per_session = int(input("Hvor mange minutter varer hver studieøkt?"))

            if study_sessions <= 0 or minutes_per_session <= 0:  # feilmeldig dersom verdien er negativ
                print("Prøv igjen")
            else:
                break

        except ValueError: # Forventer feil - og svarer på det istedenfor å kræsje
            print("Ugyldig data.")

    total_minutes = study_sessions * minutes_per_session
    hours = total_minutes // 60  # finner hele timer
    remaining_minutes = total_minutes % 60  # finner resterende minutter

    print (f"Samlet tidsbruk: {hours} timer og {remaining_minutes} minutter.")

oppgave1_1()  # Kaller tilbake funksjonen


# Oppgave 1.2 - Analyser tekst
def oppgave1_2 ():
    text = input("Skriv inn en tekst: ")

    while text =="" or text == " ":   # feilmelding dersom brukeren skriver ingenting eller kun mellomrom
        print("Feil! Må være gyldig input")
        text = input("Skriv inn en tekst: ")

    print(len(text)) # Teller antall tegn - inkludert mellomrom

    text_without_spaces = text.replace(" ", "")   # Kom opp automatisk løsning
    print(len(text_without_spaces))

    print(text.lower())

    print(text[::-1])  # snur rekkefølgen

    if "python" in text.lower():  # lower gjør alle bokstaver til små bokstaver
        print("Python in text")
    else:
        print("Python not in text")

oppgave1_2()


# Oppgave 1.3
def oppgave1_3 ():
    start_value = int(input("Startverdi: "))
    end_value = int(input("Sluttverdi: "))

    while start_value > end_value:
        print("Error")
        start_value = int(input("Startverdi: "))
        end_value = int(input("Endverdi: "))

    for number in range(start_value, end_value + 1): # +1 for å få med sluttverdien
        if number % 2 == 0:  # om tallet er helt dersom det deles på 2 uten rest
            print(number)

    for number in range(start_value, end_value + 1):
        if number % 3 == 0:  # om tallet er helt dersom det deles på 3 uten rest
            print(number)

    total = 0
    for number in range(start_value, end_value + 1):
        total = number + total

    print(total)

oppgave1_3()


# Oppgave 1.4
running = True
# Programmet kjøres på nytt helt til running = False
while running:
    print("\n1. Beregn tidsbruk")
    print("2. Analysser tekst")
    print("3. Analyser tallintervall")
    print("4. Avslutt")

    choice = input("Velg et alternativ (1-4): ")

    if choice == "1":
        oppgave1_1() # Kaller tilbake oppgavene som ligger i funksjoner - slipper å skrive alt på nytt

    elif choice == "2":
        oppgave1_2()

    elif choice == "3":
         oppgave1_3()

    elif choice == "4":
        print("Hadebra!")
        running = False

    else:
        print("Invalid option, please try again.")

