# Выполнить сортировку словаря d = {'а':1, 'b':2, 'c':3}

def do_it():
    d = {'а': 1, 'b': 2, 'c': 3}  # Создание словаря
    a = dict(d.popitem() for j in range(0, len(d)))
    print(a)
