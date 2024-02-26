import csv

with open('game.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter='$'))[1:]

    count_error = {}

    for row in reader:
        count_error[row[0]] = count_error.get(row[0], 0) + 1

    ans = []
    for row in reader:
        ans.append(count_error[row[0]])

    ans = sorted(ans)