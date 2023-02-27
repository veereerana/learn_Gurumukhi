import tkinter as tk
import random

root = tk.Tk()
root.title('lipiQuiz')
scrwd = root.winfo_screenwidth()
scrht = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (scrwd, scrht))
root.config(background="#000000")

lip = 'aAesh kKgG| cCjJ\\ tTfFx qQdDn pPbBm XrlvV S^Zz&'

P1 = [ch for ch in  lip.split()[0]]
P2 = [ch for ch in  lip.split()[1]]
P3 = [ch for ch in  lip.split()[2]]
P4 = [ch for ch in  lip.split()[3]]
P5 = [ch for ch in  lip.split()[4]]
P6 = [ch for ch in  lip.split()[5]]
P7 = [ch for ch in  lip.split()[6]]
P12 = P1+P2


P123 = P12+P3
P1234 = P123+P4
P12345 = P1234+P5
P123456 = P12345+P6
P1234567 = P123456+P7

lipi =P1234

def change():
    global letter, lipi, Lagan
    letter = random.choice(lipi)
    labeltext.configure(text=letter,font='GurbaniAkhar 540 bold')

def startquiz():
    global letter
    btnext = tk.Button(root, text='Next',foreground = ("#ffffff"), background=("#000000"), font=('Arial', 24), command=change)
    btnext.place(relx=0.9, rely=0.45)

def started():
    btn.destroy()
    startquiz()

btn = tk.Button(root, text='Start', background=("#ffffff"), font=('Arial', 24), command=started)
btn.place(relx=0.9, rely=0.45)
labeltext = tk.Label(root, text='A~Kr', foreground = ("#ffffff"), background=("#000000"), font='GurbaniAkhar 200 bold')
labeltext.place(relx=0.2)

root.mainloop()