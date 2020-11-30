# mynotebook
# autor Bulat Valiakhmetov

import tkinter
import json

root = tkinter.Tk()
root.title("mynotebook")
dicer = dict()
def clicked():
    dicer[txt_eng.get()] = txt_ru.get()
    v = txt_eng.get()
    with open('engru.json', 'a') as file:
        json.dump(dicer, file, ensure_ascii=False)
        del dicer[v]
        txt_eng.delete(0, "end")
        txt_ru.delete(0, "end")

lab1 = tkinter.Label(root, text = "english")
lab2 = tkinter.Label(root, text = "russian")
txt_eng = tkinter.Entry(root, width = 40)
txt_eng.focus()
txt_ru = tkinter.Entry(root, width = 40)
but1 = tkinter.Button(root, text = "save", command = clicked)
lab1.pack()
txt_eng.pack()
lab2.pack()
txt_ru.pack()
but1.pack()
root.mainloop()
