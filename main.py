import tkinter as tk
win = tk.Tk()


at = tk.Label(win,text = "koeficient a:")
at.pack()

a = tk.Entry(win)
a.pack()


bt = tk.Label(win,text = "koeficient b:")
bt.pack()

b = tk.Entry(win)
b.pack()


ct = tk.Label(win,text = "koeficient c:")
ct.pack()

c = tk.Entry(win)
c.pack()

def executor():
    print(a.get(),b.get(),c.get())
    ka = int(a.get())
    kb = int(b.get())
    kc = int(c.get())
    d = kb**2 -4*ka*kc
    if d<0:
        vysledok = tk.Label(win,text = "nema riesenie v R")
        vysledok.pack()
        #print("nema riesenie v R")
    elif d == 0:
        x1 = -kb/(2*ka)
        vysledok = tk.Label(win,text = x1)
        vysledok.pack()
        #print("x=", -kb/(2*ka))
    else:
        #print("x1=",(-kb+d**0.5)/(2*ka))
        #print("x2=",(-kb-d**0.5)/(2*ka))
        x1 = (-kb+d**0.5)/(2*ka)
        x2 = (-kb-d**0.5)/(2*ka)
        vysledok1 = tk.Label(win,text = x1)
        vysledok1.pack()
        vysledok2 = tk.Label(win,text = x2)
        vysledok2.pack()


button = tk.Button(win,text = "Click me!!!",command=executor)
button.pack()


win.mainloop()
