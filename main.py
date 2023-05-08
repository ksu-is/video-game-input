##########################################################################################
# Import Modules
from tkinter import *
import csv

##########################################################################################
# Database Parsing
database = []
with open('database.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    c = 0
    for line in reader:
        c += 1
        if c == 1:
            continue  # skip the csv headers
        gameEntry = []
        for col in line:
            item = col.split('|')
            platValues = []
            for i in item:
                platValues.append(i.strip())
            gameEntry.append(platValues)
        database.append(gameEntry)

# initialize backend arrays
platforms = []
genres = []
games = []

##########################################################################################
# GUI generation
root = Tk()
root.title("Video Game Input Recommender - Evan Pollifrone")
root.geometry("800x450")
root.configure(background='gray')
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

titleLabel = Label(text="Video Game Input Recommender",
                   bg="gray", fg='white', font=("Arial", 25))
titleLabel.grid(row=0, column=0, columnspan=3,
                sticky="nw", padx=10, pady=(10, 0))

platLabel = Label(text="Platform", bg="gray", fg='white', font=("Arial", 15))
platLabel.grid(row=1, column=0, sticky="nsw", padx=(10, 0), pady=10)

genreLabel = Label(text="Genre", bg="gray", fg='white', font=("Arial", 15))
genreLabel.grid(row=1, column=1, sticky="nsw", padx=(10, 0), pady=10)

gameLabel = Label(text="Game", bg="gray", fg='white', font=("Arial", 15))
gameLabel.grid(row=1, column=2, sticky="nsw", padx=10, pady=10)

for item in database:
    for plat in item[0]:
        if plat not in platforms:
            platforms.append(plat)
platforms.sort()

c = 0
platBox = Listbox(root, selectmode=SINGLE, relief=FLAT)
for plat in platforms:
    if plat == "ns":
        plat = "Nintendo Switch"
    if plat == "p4":
        plat = "Playstation 4"
    if plat == "p5":
        plat = "Playstation 5"
    if plat == "xo":
        plat = "Xbox One"
    if plat == "xsx":
        plat = "Xbox Series X"
    if plat == "pc":
        plat = "Personal Computer"
    platBox.insert(c, plat)
    c += 1

platBox.grid(row=2, column=0, sticky="nsew", padx=(10, 0))

genreBox = Listbox(root, selectmode=SINGLE, relief=FLAT)
genreBox.grid(row=2, column=1, sticky="nsew", padx=(10, 0))

gameBox = Listbox(root, selectmode=SINGLE, relief=FLAT)
gameBox.grid(row=2, column=2, sticky="nsew", padx=10)

recLabel = Label(text="Select a platform, genre, and game",
                 bg="gray", fg='white', font=("Arial", 20))
recLabel.grid(row=3, column=0, columnspan=3, sticky="sw", padx=10, pady=10)

##########################################################################################
# Logic Processor
platSel = None
genreSel = None
gameSel = None

def recommendation():
    if platSel and genreSel and gameSel:
        recLabel.configure(text="Recommendation: Controller")
    else:
        recLabel.configure(text="Error: Missing Selection")

##########################################################################################
# Events
def platCallback(event):
    global platSel
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        platSel = platforms[index]

        genres.clear()
        genreBox.delete(0,'end')

        games.clear()
        gameBox.delete(0,'end')

        for item in database:
            if platSel in item[0]:
                for genreItem in item[1]:
                    if genreItem not in genres:
                        genres.append(genreItem)
        genres.sort()

        c = 0
        for genre in genres:
            if genre == "fps":
                genre = "First Person Shooter"
            if genre == "racing":
                genre = "Racing"
            if genre == "sports":
                genre = "Sports"
            if genre == "rpg":
                genre = "Role Playing Game"
            if genre == "mmo":
                genre = "Massively Multiplayer Online"
            genreBox.insert(c, genre)
            c += 1

platBox.bind("<<ListboxSelect>>", platCallback)

def genreCallback(event):
    global platSel
    global genreSel
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        genreSel = genres[index]

        games.clear()
        gameBox.delete(0,'end')

        for item in database:
            if platSel in item[0] and genreSel in item[1]:
                games.append(item[2][0])
        games.sort()

        c = 0
        for game in games:
            gameBox.insert(c, game)
            c += 1

genreBox.bind("<<ListboxSelect>>", genreCallback)

def gameCallback(event):
    global platSel
    global genreSel
    global gameSel

    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        gameSel = games[index]

        recommendation()

gameBox.bind("<<ListboxSelect>>", gameCallback)

##########################################################################################
# Execution Loop
root.mainloop()
