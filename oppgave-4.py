# OPPGAVE 4
import csv

# Oppgave 4.1 - Les og kontroller data
valid_requests = []

try:
    with open("supporthenvendelser.csv", "r", encoding="utf-8") as file:  # "r" betyr at filen åpnes for reading
        reader = csv.DictReader(file)  # DictReader gjør hver rad til en dictionary.

        for row_number, row in enumerate(reader, start=2):  # start på 2 fordi første linje er overskriften

            # Sjekker om alle felt har verdi
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

            # Raden er gyldig og legges til i listen
            valid_requests.append({
                "id": request_id,
                "category": row["category"],
                "minutes": minutes,
                "is_resolved": row["is_resolved"]
            })

except FileNotFoundError:
    print("Filen ble ikke funnet")