# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry( "800x450" )

platBox = Listbox(root)
platBox.insert(1, "Python")
platBox.insert(2, "Perl")
platBox.insert(3, "C")
platBox.insert(4, "PHP")
platBox.insert(5, "JSP")
platBox.insert(6, "Ruby")

platBox.pack()


# Execute tkinter
root.mainloop()
