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
root.title("Video Game Input Recommender")

# Adjust size
root.geometry( "800x450" )
root.configure(background='gray')

titleLabel = Label(text = "Video Game Input Recommender", bg="gray", fg='white', font=("Arial", 25))
titleLabel.pack(anchor=N, pady=10)

c = 0
platBox = Listbox(root, selectmode=SINGLE, relief=FLAT)
for plat in platforms:
    c += 1
    if plat == "ns":
        plat = "Nintendo Switch"
    if plat == "p4":
        plat = "Playstation 4"
    if plat == "p5":
        plat = "Playstation 5"
    if plat == "x1":
        plat = "Xbox One"
    if plat == "xx":
        plat = "Xbox Series X"
    if plat == "pc":
        plat = "Computer"
    platBox.insert(c, plat)

platBox.pack(anchor=NW, padx=10, pady=10)


# Execute tkinter
root.mainloop()
