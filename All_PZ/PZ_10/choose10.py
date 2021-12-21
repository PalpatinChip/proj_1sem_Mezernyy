from All_PZ.PZ_10 import *


def chooseDo():
    ll = input("Введите номер задания\n")
    if ll == '1':
        PZ_10_1.do_it()
    elif ll == '2':
        PZ_10_2.do_it()
    else:
        print("Ошибка!")
