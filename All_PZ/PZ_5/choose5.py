from All_PZ.PZ_5 import *


def chooseDo():
    ll = input("Введите номер задания")
    if ll == 1:
        PZ_5_1.do_it()
    elif ll == 2:
        PZ_5_2.do_it()
    else:
        print("Ошибка!")
