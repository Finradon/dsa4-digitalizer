from tkinter import *
import json

root = Tk()
root.title('Zauber Hinzufügen')
l1 = Label(root, text='Name: ')
l2 = Label(root, text='Kosten: ')
l3 = Label(root, text='Zauberdauer: ')
l4 = Label(root, text='Wirkungsdauer: ')
l5 = Label(root, text='Kurzfassung: ')
l6 = Label(root, text='Langfassung: ')
label_list = [l1, l2, l3, l4, l5, l6]

for idx, label in enumerate(label_list):
    label.grid(row=idx, column=0)

name = Entry(root, borderwidth=2, width=50, font=('Helvetica', 24))
kosten = Entry(root, borderwidth=2, width=50, font=('Helvetica', 24))
zauberdauer = Entry(root, borderwidth=2, width=50, font=('Helvetica', 24))
wirkungsdauer = Entry(root, borderwidth=2, width=50, font=('Helvetica', 24))
kurz = Entry(root, borderwidth=2, width=50, font=('Helvetica', 24))
lang = Entry(root, borderwidth=2, width=50, font=('Helvetica', 24))
entry_list = [name, kosten, zauberdauer, wirkungsdauer, kurz, lang]

for idx, entry in enumerate(entry_list):
    entry.grid(row=idx, column=1)

def confirm(event=None):
    str_list = []
    
    for entry in entry_list:
        str_list.append(entry.get())
    spell = {str_list[0]: {'kosten': str_list[1], 'zauberdauer': str_list[2], 'wirkungsdauer': str_list[3], 'kurz': str_list[4], 'lang': str_list[5]}}
    
    with open('zauber.json') as file:
        zauber = json.load(file)
    
    zauber.update(spell)

    with open('zauber.json', 'w') as file:
        json.dump(zauber, file)

b1 = Button(root, text='Bestätigen', command=confirm)
b2 = Button(root, text='Abbrechen', command=root.destroy)

b1.grid(row=len(label_list), column=0)
root.bind('<Return>',lambda event=None: b1.invoke())
b2.grid(row=len(label_list), column=1)

root.mainloop()