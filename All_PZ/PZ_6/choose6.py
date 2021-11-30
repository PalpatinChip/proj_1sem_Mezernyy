from All_PZ.PZ_6 import *
from random import randint


def chooseDo():
    ll = input("Введите номер задания\n")
    if ll == '1':
        PZ_6_1.do_it()
    elif ll == '2':
        PZ_6_2.do_it()
    elif ll == '3':
        PZ_6_3.do_it()
    else:
        print("Ошибка!")
