# Arbeidskrav 1
Dina Maria Øien



### Oppgave 2:
Til oppgave 2 valgte jeg å bruke en liste med dictionaries for å lagre studieøktene, ovenfor tuple.
Dette gjorde jeg fordi hvert felt får da et tydelig navn, 
og det gjør det lettere å forstå hva verdiene betyr.
Det blir også lettere å hente ut riktig informasjon ved hjelp av feltnavnene. 
Hadde jeg brukt tuple, hadde jeg måtte hentet ut informasjonen med hjep av indeksene deres.
Listen samler studieøktene og deler de opp med navnene: topic, duration_minutes og status. 



### Oppgave 3 - Teksttilfeller:
#### Test 1 - feilmelding - negativ varighet 
Input: -5 minutter  
Resultat: feilmelding fordi verdien må være over 0

#### Test 2 - feilmelding - ugyldig datoformat
Input: 09-10-2002  
Resultat: feilmelding fordi datoen ikke er skrevet i riktig format dd.mm.yyyy

#### Test 3 - feilmelding - bokstaver i dato
Input: hei  
Resultat: feilmelding fordi dato må skrives med tall og ikke bokstaver

#### Test 4 - gyldig resultat - beregne sluttid
Input: Starttid 10:30 og varighet 45 minutter  
Resultat: viste klokkeslett 11.15 som sluttid - var forventet

#### Test 5 - gyldig resultat - gyldig dato
Input: 18.07.2009  
Resultat: programmet kjøres fordi input var gyldig i forhold til format

#### Test 6 - gyldig resultat - antall dager mellom datoer
Input: 12.03.2026 og 19.03.2026  
Resultat: programmet kjørte som det skulle og leverte resutatet: 7 dager

### Oppgave 3 - Kilder
Python-standardbibliotek - Python-dokumentasjon  
Python Software Foundation  

Tittel: datetime — Basic date and time types
https://docs.python.org/3/library/datetime.html  
Dette ble brukt for å finne informasjon om datetime, og jeg har benyttet meg av strptime(), 
strftime() og timedelta, som jeg også har funnet informasjon om her. 

Tittel: Built-in Functions  
https://docs.python.org/3/library/functions.html   
Brukt for å finne nyttig informasjon om abs(), som jeg benyttet meg av.

Tittel: Data Structures
https://docs.python.org/3/tutorial/datastructures.html   
Brukt for å finne mer relevant informasjon om .sort(), og forstå bruken bedre. Benyttet meg av dette.

