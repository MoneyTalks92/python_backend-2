import unicodedata

names = [['Kovács', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]
users = []

for surname, first_name in names:
    unaccented_first_name = unicodedata.normalize('NFKD', first_name).encode(
        'ASCII', 'ignore').decode("utf-8")
    unaccented_surname = unicodedata.normalize('NFKD', surname).encode(
        'ASCII', 'ignore').decode("utf-8")
    users.append(
        f"{surname} {first_name} {unaccented_surname.lower()}.{unaccented_first_name.lower()}@company.hu {surname}123Start "
    )

users.sort()

with open("nevek.txt", "w") as f:
    for user in users:
        f.write(f'{user} \n')