# Приложение ТОРГОВАЯ ФИРМА для автоматизированного контроля продаж
# товаров торговой фирмы. БД должна содержать таблицу Продажа товаров со следующей
# структурой записи: Дата продажи, Товар, Сумма, Скидка, Филиал, Менеджер.
# БД должна обеспечивать получение информации о продаже товаров по
# наименованию товара.

import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Main window class"""

    def __init__(self, roottt):
        super().__init__(roottt)
        self.btn_open_dialog = None
        self.tree = None
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):    # Main window
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.btn_open_dialog = tk.Button(toolbar, text='Добавить запись', command=self.open_dialog, bg='#5da130', bd=0,
                                         compound=tk.TOP)
        self.btn_open_dialog.pack(side=tk.LEFT)

        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP) 
        btn_edit_dialog.pack(side=tk.LEFT)

        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#5da130',
                               bd=0, compound=tk.TOP)
        btn_delete.pack(side=tk.LEFT)

        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP)
        btn_search.pack(side=tk.LEFT)

        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                                bd=0, compound=tk.TOP)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=(        # Tree making
            'id', 'data', 'tovar', 'cost', 'skidka', 'filial', 'manager'), height=15,
                                 show='headings')

        self.tree.column('id', width=50, anchor=tk.CENTER)
        self.tree.column('data', width=80, anchor=tk.CENTER)
        self.tree.column('tovar', width=150, anchor=tk.CENTER)
        self.tree.column('cost', width=100, anchor=tk.CENTER)
        self.tree.column('skidka', width=80, anchor=tk.CENTER)
        self.tree.column('filial', width=120, anchor=tk.CENTER)
        self.tree.column('manager', width=120, anchor=tk.CENTER)

        self.tree.heading('id', text='Код')
        self.tree.heading('data', text='Дата')
        self.tree.heading('tovar', text='Товар')
        self.tree.heading('cost', text='Магазин')
        self.tree.heading('skidka', text='Скидка')
        self.tree.heading('filial', text='Филиал')
        self.tree.heading('manager', text='Менеджер')

        self.tree.pack(side=tk.BOTTOM)

    def records(self, data, tovar, cost, skidka, filial, manager):  # inserting data
        self.db.insert_data(data, tovar, cost, skidka, filial, manager)
        self.view_records()

    def update_record(self, data, tovar, cost, skidka, filial, manager):        # updating data
        self.db.cur.execute("""UPDATE tovarDB SET data=?, tovar=?, cost=?, skidka=?, filial=?, manager=? 
        WHERE id=?""", (data, tovar.lower(), cost, skidka, filial.lower(), manager.lower(),
                        self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):             # Watch data
        self.db.cur.execute("""SELECT * FROM tovarDB""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):       # delete data
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM tovarDB WHERE id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, tovar_name):   # search data
        self.db.cur.execute(f"""SELECT * FROM tovarDB WHERE tovar LIKE '%{tovar_name.lower()}%'""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    @staticmethod
    def open_dialog():
        Child(root, app)

    @staticmethod
    def open_update_dialog():
        Update()

    @staticmethod
    def open_search_dialog():
        Search()


class Child(tk.Toplevel):
    """Дочка"""

    def __init__(self, roott, appp):
        super().__init__(roott)
        self.btn_ok = None
        self.entry_manager = None
        self.entry_filial = None
        self.entry_skidka = None
        self.var = None
        self.entry_bid = None
        self.entry_name_shop = None
        self.entry_name_tovar = None
        self.entry_id = None
        self.init_child()
        self.view = appp

    def init_child(self):       # adding new
        self.title('Добавить запись')
        self.geometry('500x300+400+300')
        self.resizable(False, False)

        label_data = tk.Label(self, text='Дата')
        label_data.place(x=50, y=25)
        self.entry_id = ttk.Entry(self)
        self.entry_id.place(x=250, y=25)

        label_name_tovar = tk.Label(self, text='Наименование товара')
        label_name_tovar.place(x=50, y=50)
        self.entry_name_tovar = ttk.Entry(self)
        self.entry_name_tovar.place(x=250, y=50)

        label_name_shop = tk.Label(self, text='Цена')
        label_name_shop.place(x=50, y=75)
        self.entry_name_shop = ttk.Entry(self)
        self.entry_name_shop.place(x=250, y=75)

        label_skidka = tk.Label(self, text='Скидка')
        label_skidka.place(x=50, y=100)
        self.entry_skidka = ttk.Entry(self)
        self.entry_skidka.place(x=250, y=100)

        label_filial = tk.Label(self, text='Филиал')
        label_filial.place(x=50, y=125)
        self.entry_filial = ttk.Combobox(self, values=[u'Юг', u'Запад', u'Центр', u'Восток', u'Север',
                                                       u'Европа', u'Азия', u'Бразилия', u'Атлантида'])
        self.entry_filial.place(x=250, y=125)

        label_manager = tk.Label(self, text='Менеджер')
        label_manager.place(x=50, y=150)
        self.entry_manager = ttk.Entry(self)
        self.entry_manager.place(x=250, y=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=220)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=220)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_id.get(),
                                                                       self.entry_name_tovar.get(),
                                                                       self.entry_name_shop.get(),
                                                                       self.entry_skidka.get(),
                                                                       self.entry_filial.get(),
                                                                       self.entry_manager.get()))
        self.grab_set()
        self.focus_set()


class Update(Child):            # Update class window
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=150, y=220)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_id.get(),
                                                                          self.entry_name_tovar.get(),
                                                                          self.entry_name_shop.get(),
                                                                          self.entry_skidka.get(),
                                                                          self.entry_filial.get(),
                                                                          self.entry_manager.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):      # Search window
    def __init__(self):
        super().__init__()
        self.entry_search = None
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:       # working with db
    def __init__(self):
        with sq.connect('torgFirm.db') as self.con:
            self.cur = self.con.cursor()
            # create new DB
            self.cur.execute("""CREATE TABLE IF NOT EXISTS tovarDB (     
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data DATE NOT NULL,
                tovar TEXT NOT NULL,
                cost FLOAT NOT NULL,
                skidka FLOAT,
                filial TEXT NOT NULL,
                manager TEXT NOT NULL
                )""")

    def insert_data(self, data, tovar, cost, skidka, filial, manager):  # inserting data
        self.cur.execute(
            """INSERT INTO tovarDB (data, tovar, cost, skidka, filial, manager) VALUES (?, 
            ?, ?, ?, ?, ?)""",
            (data, tovar.lower(), cost, skidka, filial.lower(), manager.lower()))
        self.con.commit()


if __name__ == "__main__":      # Starting
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Работа с базой данных")
    root.geometry("1000x450+300+200")
    root.resizable(False, False)
    root.mainloop()
