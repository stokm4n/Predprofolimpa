import csv

#открыть
with open('game.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter='$'))[1:]

    
    for gameName, characters, nameError, date in reader:
        if '55' in nameError:
            print(f'У персонажа {characters} в игре {gameName} нашлась ошибка с кодом {nameError}. Дата фиксации: {date}')
    #Замена данных на нужные
    for row in reader:
        if '55' in row[2]:
            row[2] = 'Done'
            row[3] = '0000-00-00'

#запись новго файла
with open('game_new.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter='$')
    writer.writerow(['GameName' , 'characters' , 'nameError', 'date'])
    writer.writerows(reader)
