# Дано вещественное число A и целое число N (>0). Используя один цикл, вывести все целые степени числа A от 1 до N.


def do_it():
    a = input("Введите число A\n")
    n = input("Введите число N\n")

    while type(a) != float:                           # обработка исключений A
        try:
            a = float(a)
        except ValueError:
            print('Введите число заново!')
            a = input('Введите число A:\n')
    while type(n) != int:                           # обработка исключений N
        try:
            n = int(n)
        except ValueError:
            print('Введите число заново!')
            n = input('Введите число N:\n')
    if n > 0:
        print(', '.join(str(int(a) ** i) for i in range(1, n+1)))           # Вывод строки из степеней
    else:
        print("Ошибка")
