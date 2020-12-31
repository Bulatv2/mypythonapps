# mynotebook
# autor Bulat

import tkinter

root = tkinter.Tk()
root.title("mynotebook")
root.geometry("350x180")
dicer = {}
def save():
    dicer[ent_eng.get()] = ent_ru.get()
    lbl3.configure(text = ent_eng.get())
    lbl4.configure(text = ent_ru.get())
    with open('enru.txt', 'a') as file:
        file.write("{}:{}\n".format(ent_eng.get(),ent_ru.get()))
        del dicer[ent_eng.get()]
        ent_eng.delete(0, "end")
        ent_ru.delete(0, "end")
lbl1 = tkinter.Label(root, text = "english")
lbl2 = tkinter.Label(root, text = "russian")
lbl3 = tkinter.Label(root, text = "")
lbl4 = tkinter.Label(root, text = "")
ent_eng = tkinter.Entry(root, width = 40)
ent_eng.focus()
ent_ru = tkinter.Entry(root, width = 40)
btn1 = tkinter.Button(root, text = "save", command = save)
lbl1.pack()
ent_eng.pack()
lbl2.pack()
ent_ru.pack()
btn1.pack()
lbl3.pack()
lbl4.pack()
root.mainloop()
