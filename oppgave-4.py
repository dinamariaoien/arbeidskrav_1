# OPPGAVE 4
import csv

# Oppgave 4.1 - Les og kontroller data
valid_requests = []   # Liste for gyldige henvendelser

try:
    with open("supporthenvendelser.csv", "r", encoding="utf-8") as file:  # "r" betyr at filen åpnes for reading
        reader = csv.DictReader(file)  # DictReader gjør hver rad til en dictionary.

        for row_number, row in enumerate(reader, start=2):  # starter bare på 2 fordi første linje er overskriften

            # Sjekker om alle feltene har en verdi
            if not row["id"] or not row["category"] or not row["minutes"] or not row["is_resolved"]:
                print(f"Rad {row_number}: Mangler verdi")
                continue

            try:
                # Gjør id og minutes om til heltall
                request_id = int(row["id"])
                minutes = int(row["minutes"])

            except ValueError:
                print(f"Rad {row_number}: ID eller minutes må være heltall")
                continue

            # ID må være positiv
            if request_id <= 0:
                print(f"Rad {row_number}: ID må være et positivt heltall")
                continue

            # Minutes må være 0 eller mer
            if minutes < 0:
                print(f"Rad {row_number}: Minutes må være 0 eller mer")
                continue

            # is_resolved må være yes eller no
            if row["is_resolved"] != "yes" and row["is_resolved"] != "no":
                print(f"Rad {row_number}: is_resolved må være yes eller no")
                continue

            # Legger gyldige henvendelser til i listen
            valid_requests.append({
                "id": request_id,
                "category": row["category"],
                "minutes": minutes,
                "is_resolved": row["is_resolved"]
            })

except FileNotFoundError:
    print("Filen ble ikke funnet")   # Feilmelding hvis filen ikke finns



# Oppgave 4.2 - Analyser data
# Antall gyldige henvendelser
number_of_requests = len(valid_requests)  # Alle gyldige hevnevdelser ligger i valid_requests[], så alle elementer i listen er gyldige
print(f"Antall gyldige henvendelser: {number_of_requests}")


# Antall henvendelser per kategori
category_count = {}  # Tom dictionary

for request in valid_requests:   # Henter category fra hver dictionary
    category = request["category"]

    if category in category_count:   # Sjekker om kategorien finns
        category_count[category] += 1  # += legger noe til verdien som finns i en variabel
    else:
        category_count[category] = 1

print(category_count)


# Samlet tidsbruk
total_minutes = 0

for request in valid_requests:
    total_minutes += request["minutes"]

print(f"Samlet tidsbruk: {total_minutes} minutter")


# Gjennomsnittlig tidsbruk
average_minutes = total_minutes / number_of_requests

print(f"Gjennomsnittlig tidsbruk: {average_minutes:.1f} minutter")  #.1f viser 1 desimal


# Teller løste og uløste henvendelser
count_resolved = 0
count_unresolved = 0

for request in valid_requests:
    if request["is_resolved"] == "yes":
        count_resolved += 1
    else:
        count_unresolved += 1

print(f"Løste henvendelser: {count_resolved}")
print(f"Uløste henvendelser: {count_unresolved}")


# Finner kategorien med flest henvendelser
most_common_category = ""

for category in category_count:
    if most_common_category == "":
        most_common_category = category

    elif category_count[category] > category_count[most_common_category]:
        most_common_category = category

print(f"Kategori med flest henvendelser: {most_common_category}")


# Lager en liste med uløste henvendelser
unresolved_requests = []  # Tom liste

for request in valid_requests:
    if request["is_resolved"] == "no":
        unresolved_requests.append(request)


# Sorterer uløste henvendelser etter tidsbruk, lengst først
def get_minutes(request):
    return request["minutes"]

unresolved_requests.sort(key=get_minutes, reverse=True)  # Reverse viser lengsst først

print("Uløste henvendelser:")

for request in unresolved_requests:
    print(request)



# Oppgave 4.3 - Skrive rapport
with open("support-rapport.txt", "w", encoding="utf-8") as file:

    file.write("RAPPORT\n")  # Overskrift

    file.write(f"Antall gyldige henvendelser: {number_of_requests}\n")

    file.write("\nAntall i hver kategori\n")
    for category in category_count:
        file.write(f"{category}: {category_count[category]}\n")

    file.write("\nTidsbruk\n")
    file.write(f"Samlet tidsbruk: {total_minutes} minutter\n")
    file.write(f"Gjennomsnittlig tidsbruk: {average_minutes:.1f} minutter\n")

    file.write("\nStatus på henvendelsene\n")
    file.write(f"Løste henvendelser: {count_resolved}\n")
    file.write(f"Uløste henvendelser: {count_unresolved}\n")

    file.write("\nFlest henvendelser\n")
    file.write(f"{most_common_category}\n")

    file.write("\nUløste henvendelser\n")

    for request in unresolved_requests:
        file.write(
            f"ID: {request['id']}, "
            f"Kategori: {request['category']}, "
            f"Minutter: {request['minutes']}\n"
        )


# Oppgave 4.4 - Finn og rett feil
def sum_resolved_minutes(requests: list[dict[str, str | int]]) -> int:
    total = 0
    for request in requests:
        if request["is_resolved"] == "yes":  # Endret fra = til ==
            total += request["minutes"]  # Endret til += fordi det skal legges til verdi, ikke erstatte
    return total  # Endret fra total_minutes til total, fordi total_minutes er ikke en eksisterende variabel i denne funksjonen

print(sum_resolved_minutes(valid_requests)) # lat til valid_requests i (), fordi funksjonen trenger en liste å kjøre
