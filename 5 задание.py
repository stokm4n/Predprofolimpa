import csv


def generate_cashe(s: str):
    alphabet = 'йцукенгшщзхъфывапролджэячсмтьбю ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
    d = {n: i for i, n in enumerate(alphabet, 1)}
    p = 65
    m = 10 ** 9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)


with_hash = []
with open('game.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter='$'))[1:]
    for row in reader:
        row[0] = generate_cashe(row[1])
        with_hash.append(row)

with open('game.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['GameName,characters,gameError,date'])
    writer.writerows(with_hash)
