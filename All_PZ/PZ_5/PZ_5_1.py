# С помощью функции получить вертикальную и горизонтальную линии. Линия проводится многократной печатью символа.
# Заключить слово в рамку из символов

def do_it():      # Объявление функции
    x = int(input('Введите горизонталь: '))
    y = int(input('Введите вертикаль: '))
    word = input('Введите слово: ')
    x = len(word) + 2 if x < len(word) + 2 else x       # Проверка размеров границ коробки

    for i in range(0, y):
        if i == 0 or i == y - 1:
            print('|' + '-' * (x - 2) + '|')            # Печать верха и низа коробки
        elif i == int(y // 2):
            print('|' + word.center(x - 2) + '|')       # Печать строки со словом
        else:
            print('|' + ' ' * (x - 2) + '|')            # Печать пустых строк
