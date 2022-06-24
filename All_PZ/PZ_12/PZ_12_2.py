import tkinter as tk


class Main(tk.Frame):                                                                                                   # Main class
    def __init__(self, roottt):
        super().__init__(roottt)



        tk.Label(text="ПЗ-4", bg="#3766D5", fg="white", font=("Arial", 24)).place(x=20, y=20)

        tk.Label(bg="#3766D5", fg="white", font=("Arial", 14), text="Дано вещественное число A и целое число N ("   # Description
                                                                    ">0). Используя один цикл, вывести всe\n "
                                                                    "целые "
                                                                    "степени числа A от 1 до N.").place(x=20, y=120)

        a = tk.IntVar()
        n = tk.IntVar()
        tk.Entry(bg='white', fg='black', font=('comforta', 15), borderwidth=1, textvariable=a).place(x=20, y=220,
                                                                                                     width=300,
                                                                                                     height=25)
        tk.Entry(bg='white', fg='black', font=('comforta', 15), borderwidth=1, textvariable=n).place(x=20, y=270,
                                                                                                     width=300,
                                                                                                     height=25)

        def do_it():
            if n.get() > 0:
                lab.configure(text=', '.join(str(a.get() ** i) for i in range(1, n.get() + 1)))  # Вывод строки из
                # степеней
            else:
                lab.configure(text="Ошибка")

        lab = tk.Label(text='', bg="#3766D5", fg="white", font=("Arial", 14))
        lab.place(x=20, y=370)

        tk.Button(text="*", bg="green", bd=1, fg="white", font=("Arial", 14), command=do_it).place(x=275, y=470)
        tk.Label(text="Рассчитать", bg="#3766D5", fg="white", font=("Arial", 14)).place(x=325, y=470)


if __name__ == "__main__":                                                                                          # Start
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("ПЗ 12")
    root.geometry("800x650+300+200")
    root.configure(bg="#3766D5")
    root.resizable(False, False)
    root.mainloop()
