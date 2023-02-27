import tkinter as tk
import random

root = tk.Tk()
root.title('lipiQuiz')
scrwd = root.winfo_screenwidth()
scrht = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (scrwd, scrht))
root.config(background="#000000")

P1 = ['a', 'A', 'e', 's', 'h']

lipi =P1

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