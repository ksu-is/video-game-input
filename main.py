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

print(database)

# create unique list of platforms
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
    c += 1
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

platBox.grid(row=2, column=0, sticky="nsew", padx=(10, 0))

genreBox = Listbox(root, selectmode=SINGLE, relief=FLAT)
genreBox.grid(row=2, column=1, sticky="nsew", padx=(10, 0))

c = 0
gameBox = Listbox(root, selectmode=SINGLE, relief=FLAT)
for game in games:
    c += 1
    gameBox.insert(c, game)

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
    if not platSel and not genreSel and not gameSel:
        pass
    else:
        recLabel.configure(text="Error: Missing Selection")

##########################################################################################
# Events
def platCallback(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        platSel = platforms[index]
      #  recLabel.configure(text=platSel)

        genres = []
        genreBox.delete(0,'end')

        games = []
        gameBox.delete(0,'end')

        for item in database:
            if platSel in item[0]:
                for genreItem in item[1]:
                    if genreItem not in genres:
                        genres.append(genreItem)
        genres.sort()

        c = 0
        for genre in genres:
            c += 1
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


platBox.bind("<<ListboxSelect>>", platCallback)

# On platform click
    # Clear the game box
    # Go through the data array
        # Populate the Genre box if platfrom matches

# On genre box click
    # Go through the data array
        # Populate if platform and genre match

# On game box click
    # Give recommendation

# Clear selections

##########################################################################################
# Execution Loop
root.mainloop()
