import random


def res():                                                          # Main func
    def gen_dict():                                                 # Generate dictionary
        dicti = []
        i = 0
        while i < 10:
            dicti.append(random.randint(-100, 100))
            i += 1
        return dicti

    def print_res_zad1(bigdict):                                    # print results of first and second tasks
        return (f"Изначальный список: {bigdict[0]}\n"
                f"Положительный список и его длина: {bigdict[1]}, {bigdict[3]}\n"
                f"Отрицательный список и его длина: {bigdict[2]}, {bigdict[4]}")

    def print_res_zad2(dicti):
        return dicti

    def ask_zad():                                                  # ask for task number and execution
        print("""Вы выбрали задание 13. Выберите подзадание: 
              1. Организовать и вывести последовательность из N случайных целых чисел. Из
              исходной последовательности организовать последовательность, содержащую
              положительные числа и последовательность, содержащую отрицательные числа. Найти
              количество элементов в полученных последовательностях.
              2. Составить генератор (yield), который выводит из строки только цифры.\n""")
        re = input()
        return re

    ress = ask_zad()
    while True:
        if ress == "1":
            print(print_res_zad1(zad_1(gen_dict())))
            break
        elif ress == "2":
            print(print_res_zad2(zad_2()))
            break
        else:
            print("Введён неверный номер задания, начинаю процедуру заново.")


def zad_1(diction):                             # First task
    poz, neg = [], []
    for i in diction:
        if i >= 0:
            poz.append(i)
        else:
            neg.append(i)
    return diction, poz, neg, len(poz), len(neg)


def zad_2():                                    # Second task
    stroka = "Во1 и п0м3р д3д М4ксим"
    a = []

    def find_digit():                           # generator
        for i in stroka:
            if i.isdigit():
                yield i

    gen = find_digit()
    for y in gen:
        a.append(y)
    return a, stroka
