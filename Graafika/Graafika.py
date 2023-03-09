from tkinter import *
from math import *

def deiskriminant(a, b, c):
    try:
        diskriminant= b**2 -4*a*c
        if diskriminant < 0:
            return None, None
        else:
            root1 = (-b + diskriminant**0.5) / (2*a)
            root2 = (-b - diskriminant**0.5) / (2*a)
            return root1, root2
    except ZeroDivisionError:
        if b==0:
            return None, None
        else:
            root = -c/b
            return root, None

def lahenda_klikkid():
    a = float(ent1.get())
    b = float(ent2.get())
    c = float(ent3.get())

    root1, root2 = deiskriminant(a,b,c)
    if root1 is None:
        print("Error", "The equation has no real roots.")
    elif root2 is None:
        print("Solution", f"The equation has one root: {root1:.2f}")
    else:
        print("Solution", f"The roots are: {root1:.2f} and {root2:.2f}")

def txt_to_lbl(event):
    t=btn.get()
    lbl0.configure(text=lahenda_klikkid)
    
aken=Tk()
aken.geometry("800x600")
aken.title("Ruutvõrrandi lahendus")

lbl=Label(aken,text="Ruutvõrrandi lahendus",bg="gold",fg="#AA4A44",font="Arial 20",height=5,width=20)
ent1=Entry(aken,fg="blue",bg="lightblue",width=3,font="Arial 20",justify=LEFT)
lbl1=Label(aken,text="x**2+",font="Arial 20",height=5,width=10)
ent2=Entry(aken,fg="blue",bg="lightblue",width=3,font="Arial 20",justify=LEFT)
lbl2=Label(aken,text="x+",font="Arial 20",height=5,width=10)
ent3=Entry(aken,fg="blue",bg="lightblue",width=3,font="Arial 20",justify=LEFT)
lbl3=Label(aken,text="=0",font="Arial 20",height=5,width=10)
btn=Button(aken,text="Lahenda",fg="blue",bg="lightblue",width=10,font="Arial 20",justify=LEFT, command=lahenda_klikkid)
lbl0=Label(aken,text="Ruutvõrrandi lahendus",bg="gold",fg="#AA4A44",font="Arial 20",height=5,width=20)


lbl.pack()
ent1.pack(side=LEFT)
lbl1.pack(side=LEFT)
ent2.pack(side=LEFT)
lbl2.pack(side=LEFT)
ent3.pack(side=LEFT)
lbl3.pack(side=LEFT)
btn.pack(side=LEFT)
lbl0.place(x=235,y=450)
aken.mainloop()

