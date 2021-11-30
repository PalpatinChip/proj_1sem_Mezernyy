from All_PZ.PZ_4 import *


def chooseDo():
    ll = input("Введите номер задания\n")
    if ll == '1':
        PZ_4_1.do_it()
    elif ll == '2':
        PZ_4_2.do_it()
    else:
        print("Ошибка!")
