from All_PZ.PZ_7 import *


def chooseDo():
    ll = input("Введите номер задания\n")
    if ll == '1':
        PZ_7_1.do_it()
    elif ll == '2':
        PZ_7_2.do_it()
    else:
        print("Ошибка!")
