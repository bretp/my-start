#ze zadaného jména a příjmení sestaví uživatelské jméno s max 14 znaky
import unicodedata

def uzivjmeno():
    jmeno = input ('Zadej jméno: ')
    prijmeni = input ('Zadej prijmeni: ')
    celejmeno = prijmeni + '.' + jmeno
    uziv = celejmeno.lower()
    # odstranění diakritiky
    uziv = unicodedata.normalize('NFKD', uziv)
    output = ''
    for c in uziv:
        if not unicodedata.combining(c):
            output += c
    return output[:14]

print(uzivjmeno())
