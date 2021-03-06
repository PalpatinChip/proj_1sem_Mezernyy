# Дано трехзначное число. Используя одну операцию деления нацело, вывести первую цифру данного числа (сотни).

def do_it():
    while True:                                                             # Выполнение программы до вывода результатов
        a = input("Введите число\n")
        while type(a) != int:
            try:                                                            # Обработка исключений по типу данных
                a = int(a)
            except ValueError:
                print('Вы ввели неправильные данные! Введите целое число')
                a = input("Введите число\n")
        if a // 1000 == 0 and (a % 100 // 10 != 0 or a % 1000 // 100 != 0) and str(a)[0] != 0:  # Проверка трёхзначности
            print(a // 100)                                                 # Вывод разряда сотен
            break                                                           # Прекращение программы
        else:
            print("Введено НЕ трёхзначное число")
