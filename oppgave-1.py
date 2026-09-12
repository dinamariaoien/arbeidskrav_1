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
text = input("Write a text here:")

while text =="" or text == " ":
    print("Må være tekst")
    text = input("Write a text here:")

print(len(text))

text_without_spaces = text.replace(" ", "")   # kom opp automatisk
print(len(text_without_spaces))

print(text.lower())

print(text[::-1])

if "python" in text.lower():
    print("Python in text")
else:
    print("Python not in text")


# Oppgave 1.3
start_value = int(input("Startverdi: "))
end_value = int(input("Endverdi: "))

while start_value > end_value:
    print("Error")
    start_value = int(input("Startverdi: "))
    end_value = int(input("Endverdi: "))

for number in range(start_value, end_value + 1):
    if number % 2 == 0:
        print(number)

for number in range(start_value, end_value + 1):
    if number % 3 == 0:
        print(number)

total = 0
for number in range(start_value, end_value + 1):
    total = number + total

print(total)


# Oppgave 1.4
running = True

while running:
    print("\n1. Beregn tidspunkt")
    print("2. Analysser tekst")
    print("3. Analyser tallintervall")
    print("4. Avslutt")

    choice = input("Velg et alternativ (1-4): ")

    if choice == "1":
        print(f"")

    elif choice == "2":
        print(f"")

    elif choice == "3":
         print(f"")

    elif choice == "4":
        print("")
        running = False

    else:
        print("Invalid option, please try again.")
