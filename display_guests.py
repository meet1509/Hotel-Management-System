from tkinter import ttk
import tkinter as tk
from guests import Guest

#gui for displaying guests

#treeview for displaying db table
root = tk.Tk()
root.title("Display All Guests")
style = ttk.Style()
style.configure("Treeview.Heading", font=("Comic Sans MS", 16)) 
style.configure("Treeview",rowheight=25) 

tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="User Id")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="Name")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="Phone No.")

tree.column("#4", anchor=tk.CENTER)

tree.heading("#4", text="Room No.")

tree.column("#5", anchor=tk.CENTER)

tree.heading("#5", text="Check In")

tree.column("#6", anchor=tk.CENTER)

tree.heading("#6", text="Check Out")

tree.column("#7", anchor=tk.CENTER)

tree.heading("#7", text="Amount")

tree.pack()
   
guest = Guest()
rows = guest.display()  

for row in rows:

    print(row) 

    tree.insert("", tk.END, values=row)        




root.mainloop()