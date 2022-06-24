import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):  # Класс окна
    def __init__(self, roottt):
        super().__init__(roottt)
        self.label_list = ["University", "Institute", "Branch", "Degree", "Average CPI", "Experience", "Your website "
                                                                                                       "or blog"]
        # Список лэйблов
        self.yy = 130

        tk.Label(text="Registration details", bg="#3766D5", fg="white", font=("Arial", 24)).place(x=20, y=20)
        for i in self.label_list:
            tk.Label(text=i + " :", bg="#3766D5", fg="white", font=('comforta', 16)).place(x=350, y=self.yy, anchor="e")
            # Создание лэйблов
            self.yy += 50

        tk.Entry(bg='white', fg='black', font=('comforta', 15), borderwidth=1).place(x=350, y=120,
                                                                                     width=300, height=25)
        tk.Entry(bg='white', fg='black', font=('comforta', 15), borderwidth=1).place(x=350, y=170,
                                                                                     width=300, height=25)
        aboba = ttk.Combobox(font=('comforta', 15), values=[u"--Select--", u"First", u"Second"])
        aboba.current(0)
        aboba.place(x=350, y=220, width=300, height=25)

        aboba2 = ttk.Combobox(font=('comforta', 15), values=[u"--Select--", u"Bachelor", u"PhD"])
        aboba2.current(0)
        aboba2.place(x=350, y=270, width=110, height=25)

        rad_var = tk.IntVar()  # Radio buttons
        rad_var.set(0)
        tk.Radiobutton(bg="#3766D5", fg="black", variable=rad_var, value=0).place(x=480, y=270)
        tk.Label(text="Pursuing", bg="#3766D5", fg="white", font=("Arial", 14)).place(x=520, y=270)
        tk.Radiobutton(bg="#3766D5", fg="black", variable=rad_var, value=1).place(x=600, y=270)
        tk.Label(text="Completed", bg="#3766D5", fg="white", font=("Arial", 14)).place(x=640, y=270)

        tk.Entry(bg="white", fg="black").place(x=350, y=320, width=30, height=25)
        tk.Label(text="Upto", bg="#3766D5", fg="white", font=("Arial", 14)).place(x=380, y=320)
        tk.Entry(bg="white", fg="black").place(x=450, y=320, width=30, height=25)
        tk.Label(text="Th Semester", bg="#3766D5", fg="white", font=("Arial", 14)).place(x=480, y=320)

        tk.Entry(bg="white", fg="black").place(x=350, y=370, width=80, height=25)
        tk.Label(text="Years", bg="#3766D5", fg="white", font=("Arial", 14)).place(x=380, y=370)

        tk.Entry(bg="white", fg="black").place(x=350, y=420, width=300, height=25)

        tk.Button(text="<", bg="green", bd=1, fg="white", font=("Arial", 14)).place(x=275, y=470)
        tk.Label(text="Step 2", bg="#3766D5", fg="white", font=("Arial", 14)).place(x=325, y=470)
        tk.Button(text=">", bg="green", bd=1, fg="white", font=("Arial", 14)).place(x=400, y=470)


if __name__ == "__main__":  # Code starting
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("ПЗ 12")
    root.geometry("800x650+300+200")
    root.configure(bg="#3766D5")
    root.resizable(False, False)
    root.mainloop()
