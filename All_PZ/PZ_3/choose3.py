from All_PZ.PZ_3 import *


def chooseDo():
    ll = input("Введите номер задания")
    if ll == 1:
        PZ_3_1.do_it()
    elif ll == 2:
        PZ_3_2.do_it()
    else:
        print("Ошибка!")
