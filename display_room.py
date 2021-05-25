from tkinter import ttk
import tkinter as tk
from rooms import Room

#gui for displaying rooms

#treeview for displaying db table
root = tk.Tk()
root.title("Display All Rooms")
style = ttk.Style()
style.configure("Treeview.Heading", font=("Comic Sans MS", 16)) 
style.configure("Treeview",rowheight=25) 

tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="Room No.")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="Price")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="Category")

tree.column("#4", anchor=tk.CENTER)

tree.heading("#4", text="Available")

tree.pack()
   
room = Room()

rows = room.display()  

for row in rows:

    print(row) 

    tree.insert("", tk.END, values=row)        




root.mainloop()