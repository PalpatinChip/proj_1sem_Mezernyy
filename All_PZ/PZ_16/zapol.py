import random
import sqlite3 as sq

tovar = ['Яблоки', "Апельсины", "Бананы", "Души"]
filial = ['Юг', 'Запад', 'Центр', 'Восток', 'Север',
          'Европа', 'Азия', 'Бразилия', 'Атлантида']
manager = ['First', 'Second', 'Third']

with sq.connect('torgFirm.db') as con:
    cur = con.cursor()
    i = 0
    while i <= 500:
        date = str(random.randint(1, 30)) + '.' + str(random.randint(1, 12)) + '.' + str(random.randint(1999, 2022))
        cost = random.randint(100, 10000)
        skidka = random.randint(0, 90)

        cur.execute(
            """INSERT INTO tovarDB (data, tovar, cost, skidka, filial, manager) VALUES (?, 
            ?, ?, ?, ?, ?)""",
            (date, tovar[random.randint(0, 3)].lower(), cost, skidka, filial[random.randint(0, 8)].lower(),
             manager[random.randint(0, 2)].lower()))
        con.commit()
        i += 1
