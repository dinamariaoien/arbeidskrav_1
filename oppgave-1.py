# Oppgave 1.1 - Beregn tidsbruk
study_sessions = int(input("Antall studieøkter:"))
minutes_per_session = int(input("Hvor mange minutter varer hver studieøkt?"))

while study_sessions <= 0 or minutes_per_session <= 0:
    print("Prøv igjen")
    study_sessions = int(input("Antall studieøkter:"))
    minutes_per_session = int(input("Hvor mange minutter varer hver studieøkt?"))

total_minutes = study_sessions * minutes_per_session
hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print (f"Samlet tidsbruk: {hours} timer og {remaining_minutes} minutter.")

# hvordan ikke akseptere tekst? try except


# Oppgave 1.2 - Analyser tekst
text = input()
