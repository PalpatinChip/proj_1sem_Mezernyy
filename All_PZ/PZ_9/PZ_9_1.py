# Книжные магазины предлагают следующие коллекции книг.
# Магистр — Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги - Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет — Пушкин, Достоевский, Маяковский.
# Галерея — Чехов, Тютчев, Пушкин.

# Определить:
# 1.в каких магазинах можно одновременно нельзя приобрести книги Достоевского и Пушкина.
# 2.в ассортимент магазина Галерея добавить автора Грибоедов.
# З.какие книги из магазина ДомКниги отсутствуют в магазине Галерея.

def do_it():
    mag = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
    dom = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
    buk = {'Пушкин', 'Достоевский', 'Маяковский'}
    gal = {'Чехов', 'Тютчев', 'Пушкин'}

    prov = {'Достоевский', 'Пушкин'}

    # Первая часть
    print('Есть ли Пушкин и Достоевский в...')
    print('В Магистре? ' + str(mag >= prov))                # Проверки содержания и вывод
    print('В ДомКниги? ' + str(dom >= prov))
    print('В БукМаркет? ' + str(buk >= prov))
    print('В Галерее? ' + str(gal >= prov))

    # Вторая часть
    print('\n' + str(gal))                                  # Вывод через строку старой Галереи
    gal.add('Грибоедов')                                    # Добавление Грибоедова
    print(gal)                                              # Вывод

    # Третья часть
    print('\n' + str(dom - gal))                            # Вывод через строку разницы между домом и галереей
