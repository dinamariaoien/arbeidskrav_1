# Oppgave 3 - Funksjoner og dokumentasjon
from datetime import datetime, timedelta  # Importerer data fra standarbiblioteket

# En funksjon som tar imot en dato på formatet dd.mm.åååå og returnerer en datoverdi når teksten er gyldig
def find_date(date_input):
    date = datetime.strptime(date_input, '%d.%m.%Y') # Gjør om tekst til datoverdi
    return date

while True:
    try:
        date_input = input("Skriv inn en dato (dd.mm.yyyy): ")
        found_date = find_date(date_input)
        break
    except ValueError:
        print("Skriv fullstendig dato i form: dd.mm.yyyy")

print(found_date)


# En funksjon som tar imot starttidspunkt og minutter og returnerer sluttid
def calculate_end_time(start_time, minutes):
    end_time = start_time + timedelta(minutes=minutes)  # minutes (1) sier at tidsmengden skal være i minutter og minutes (2) er vaiablen
    return end_time

while True:
    try:
        start_time_input = input("Skriv inn starttidspunkt (tt:mm): ")
        start_time = datetime.strptime(start_time_input, "%H:%M")
        break
    except ValueError:
        print("Skriv gyldig tidspunkt i form: tt:mm")

while True:
    try:
        minutes = int(input("Hvor lenge varer studieøkten?"))

        if minutes > 0:
            break
        else:
            print("Varigheten må være over 0 minutter")

    except ValueError:
        print("Varigheten må være heltall")

end_time = calculate_end_time(start_time, minutes) # Kom opp automatisk i programmet

print(end_time.strftime("%H:%M"))


# En funksjon som tar imot to datoer og returnerer positivt antall dager mellom dem
def calculate_days(date1, date2):
    difference = date2 - date1
    return abs(difference.days)  # absoluttverdi - gjør at hvis forskjellen er -5 dager, blir det 5 dager forskjell

while True:
    try:
        date1_input = input("Skriv inn dato 1: ")
        date1 = find_date(date1_input)

        date2_input = input("Skriv inn dato 2: ")
        date2 = find_date(date2_input)
        break
    except ValueError:
        print("Skriv gyldig dato i form: dd.mm.yyyy")

difference_in_days = calculate_days(date1, date2)
print(f"Mellom datoene er det {difference_in_days} dager.")


# En funksjon som tar imot en list med datoer og returnerer en kronologisk sortert list
def sort_dates(date_list):
    date_list.sort()  # .sort() sorterer datoene
    return date_list

date_list = []

for i in range (5):
    while True:
        try:
            date_input = input("Skriv inn dato dato til sortering (dd.mm.yyyy): ")
            date = find_date(date_input)
            date_list.append(date)
            break
        except ValueError:
            print ("Skriv inn gyldig dato i formatet dd.mm.yyyy")

sorted_dates = sort_dates(date_list)

print("Datoer i kronologisk rekkefølge:")

for date in sorted_dates:
    print(date.strftime("%d.%m.%Y"))



