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

genres = []

games = []

# Create object
root = Tk()
root.title("Video Game Input Recommender")

# Adjust size
root.geometry( "800x450" )
root.configure(background='gray')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

titleLabel = Label(text = "Video Game Input Recommender", bg="gray", fg='white', font=("Arial", 25))
titleLabel.grid(row=0, column=0, sticky="nsew", pady=10)

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

platBox.grid(row=1, column=0, padx=10, pady=10)

c = 0
genreBox = Listbox(root, selectmode=SINGLE, relief=FLAT)
for genre in genres:
    c += 1
    if genre == "ns":
        genre = "Nintendo Switch"
    if genre == "p4":
        genre = "Playstation 4"
    if genre == "p5":
        genre = "Playstation 5"
    if genre == "x1":
        genre = "Xbox One"
    if genre == "xx":
        genre = "Xbox Series X"
    if genre == "pc":
        genre = "Computer"
    genreBox.insert(c, genre)

genreBox.grid(row=1, column=1, padx=10, pady=10)

c = 0
gameBox = Listbox(root, selectmode=SINGLE, relief=FLAT)
for game in games:
    c += 1
    gameBox.insert(c, game)

gameBox.grid(row=1, column=2, padx=10, pady=10)


# Execute tkinter
root.mainloop()
