from tkinter import *
import json

file_name = 'test.json'

with open(file_name) as artifact_file:  # open file as data variable
    data = json.load(artifact_file)


def write_json(data, filename='test.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def add_to_json():
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
master.title(f"Adding items to {file_name}")
master.geometry("600x300+150+150")
Label(master, text="Shop Type", font=("Helvetica", 18)).grid(row=0)
Label(master, text="Rarity Type", font=("Helvetica", 18)).grid(row=1)
Label(master, text="Item Name", font=("Helvetica", 18)).grid(row=2)
Label(master, text="Item Price", font=("Helvetica", 18)).grid(row=3)
Label(master, text="Item Description", font=("Helvetica", 18)).grid(row=4)

shop_type = Entry(master, width=60, bd=4)
rarity_type = Entry(master, width=60, bd=4)
item_name = Entry(master, width=60, bd=4)
item_price = Entry(master, width=60, bd=4)
item_description = Entry(master, width=60, bd=4)

shop_type.grid(row=0, column=1)
rarity_type.grid(row=1, column=1)
item_name.grid(row=2, column=1)
item_price.grid(row=3, column=1)
item_description.grid(row=4, column=1)


Button(master, text='Add', command=add_to_json, width=50, bg='grey').grid(row=6, column=1, sticky=NW, pady=4)

mainloop()
