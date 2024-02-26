import csv

with open('game.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter='$'))[1:]
    ans = []
    name = input()
    while name != 'game':
        for gameName, characters, nameError, date in reader:
            if name == characters:
                ans.append(gameName)
                print(*ans[:5])
                break
        else:

        name = input()
