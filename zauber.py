from tkinter import *
import json

root = Tk()
root.title('Zauber Hinzufügen')
l1 = Label(root, text='Name: ')
l2 = Label(root, text='Probe: ')
l3 = Label(root, text='Kosten: ')
l4 = Label(root, text='Zauberdauer: ')
l5 = Label(root, text='Wirkungsdauer: ')
l6 = Label(root, text='Zielobjekt: ')
l7 = Label(root, text='Reichweite: ')
l8 = Label(root, text='Kurzfassung: ')
l9 = Label(root, text='Langfassung: ')
l10 = Label(root, text='Modifikationen: ')
l11 = Label(root, text='Reversalis: ')
l12 = Label(root, text='Antimagie: ')
l13 = Label(root, text='Merkmale: ')
l14 = Label(root, text='Komplexität: ')
l15 = Label(root, text='Verbreitung: ')


label_list = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15]

for idx, label in enumerate(label_list):
    label.grid(row=idx, column=0)

entry_list = []
for _ in range(len(label_list)):
    entry_list.append(Entry(root, borderwidth=2, width=50, font=('Helvetica', 24)))

for idx, entry in enumerate(entry_list):
    entry.grid(row=idx, column=1)

def confirm(event=None):
    str_list = []
    
    for entry in entry_list:
        str_list.append(entry.get())
    spell = {str_list[0]: { 'probe': str_list[1],
                            'kosten': str_list[2],
                            'zauberdauer': str_list[3],
                            'wirkungsdauer': str_list[4],
                            'zielobjekt': str_list[5],
                            'reichweite': str_list[6],
                            'kurz': str_list[7],
                            'lang': str_list[8],
                            'modifikationen': str_list[9],
                            'reversalis': str_list[10],
                            'antimagie': str_list[11],
                            'merkmale': str_list[12],
                            'komplexitaet': str_list[13],
                            'verbreitung': str_list[14]
                            }}
    
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