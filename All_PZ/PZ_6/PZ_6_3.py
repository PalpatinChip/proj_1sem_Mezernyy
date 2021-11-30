# Дан список размера N. Осуществить циклический сдвиг элементов списка вправо на
# одну позицию (при этом А1 перейдет в А2, А2 — в A3,..., АN— в А1.
from random import randint


def do_it():
    n = int(input("Введите длину списка:\n"))
    a = []
    if n >= 0:                                      # Проверка
        i = 0
        for i in range(n):
            a.append(randint(-100, 100))            # Создание списка длины N
        print(a)                                    # Вывод до изменений
        elem1 = a[-1]
        for i, elem2 in enumerate(a):               # Перечисление
            a[i], elem1 = elem1, elem2              # Смещение
        print(a)                                    # Вывод
    else:
        print("Ошибка")
