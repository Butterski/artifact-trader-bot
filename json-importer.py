from tkinter import *
import json

with open('test.json') as artifact_file:  # open file as data variable
    data = json.load(artifact_file)


def write_json(data, filename='test.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def show_entry_fields():
    # shop_type.get(), rarity_type.get(), item_name.get(), item_price.get(), item_description.get()

    y = {"name": f'{item_name.get()}',
         "price": f'{item_price.get()}',
         "description": f'{item_description.get()}'
         }

    temp = data["artifacts"][shop_type.get()]["rarity"][rarity_type.get()]
    print(temp)
    print(y)
    temp.append(y)
    write_json(data)
    item_name.delete(0, END)
    item_price.delete(0, END)
    item_description.delete(0, END)


master = Tk()
master.minsize(100, 100)
Label(master, text="Shop Type", font=("Helvetica", 18)).grid(row=0)
Label(master, text="Rarity Type", font=("Helvetica", 18)).grid(row=1)
Label(master, text="Item Name", font=("Helvetica", 18)).grid(row=2)
Label(master, text="Item Price", font=("Helvetica", 18)).grid(row=3)
Label(master, text="Item Description", font=("Helvetica", 18)).grid(row=4)

shop_type = Entry(master, width=50)
rarity_type = Entry(master, width=50)
item_name = Entry(master, width=50)
item_price = Entry(master, width=50)
item_description = Entry(master, width=50)

shop_type.grid(row=0, column=1)
rarity_type.grid(row=1, column=1)
item_name.grid(row=2, column=1)
item_price.grid(row=3, column=1)
item_description.grid(row=4, column=1)

Button(master, text='Add', command=show_entry_fields).grid(row=65, column=1, sticky=W, pady=4)

mainloop()
