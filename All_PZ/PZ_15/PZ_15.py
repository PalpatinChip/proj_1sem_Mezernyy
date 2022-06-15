from random import uniform as uni


def res():
    matrix = [                                              # matrix generation
        [
            int(uni(-5, 5)) for i in range(5)
        ]
        for j in range(5)
    ]

    def zad1():                                             # first task
        print("Начальная матрица: ")
        print(*matrix, sep='\n')
        count = 0
        for i in range(1, len(matrix), 2):                  # find all even columns
            for j in range(len(matrix[i])):
                count += matrix[j][i]
            print(f"Сумма элементов столбца: {count}")
            count = 0

    def zad2():
        print("Начальная матрица: ")
        print(*matrix, sep='\n')
        print(f"Минимальный элемент предпоследней строки: {min(matrix[-2])}")   # print min digit

    def ask_zad():
        print("""Вы выбрали задание 15. Выберите подзадание: 
              1. Для каждого столбца матрицы с четным номером найти сумму ее элементов.
              2. В матрице найти минимальный элемент в предпоследнем столбце.\n""")
        re = input()
        return re

    ress = ask_zad()
    while True:
        if ress == "1":
            print(zad1())
            break
        elif ress == "2":
            print(zad2())
            break
        else:
            print("Введён неверный номер задания, начинаю процедуру заново.")

