# Import module
from tkinter import *
import csv

database = []
with open('database.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    c = 0
    for row in reader:
        c += 1
        if c == 1:
            continue
        thing = []
        for col in row:
            item = col.split('|')
            values = []
            for i in item:
                values.append(i.strip())
            thing.append(values)
        database.append(thing)

#print(database)
#exit(-1)

platforms = []
for item in database:
    for plat in item[0]:
        if plat not in platforms:
            platforms.append(plat)

platforms.sort()

# Create object
root = Tk()

# Adjust size
root.geometry( "800x450" )

c = 0

platBox = Listbox(root)
for plat in platforms:
    c += 1
    platBox.insert(c, plat)

platBox.pack()


# Execute tkinter
root.mainloop()
