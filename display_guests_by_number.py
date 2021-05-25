from tkinter import *
from tkinter import ttk
import tkinter as tk
from guests import Guest
from tkinter import messagebox

#gui for displaying guests

def search():

    tree.delete(*tree.get_children())
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
    room_no = int(roomNo.get())
    rows = guest.display_current_guests_by_room(room_no) 
    if len(rows)==0:
        messagebox.showinfo("Guest not found", "No such guest found!")
        return
    for row in rows:
        print(row) 
        tree.insert("", tk.END, values=row)    
   
#treeview for displaying db table
root = tk.Tk()
root.geometry("1400x400")
root.title("search")

style = ttk.Style()
style.configure("Treeview.Heading", font=("Comic Sans MS", 16)) 
style.configure("Treeview",rowheight=25) 
tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')
#Entry box
roomNo = Entry(root, width=30)
roomNo.pack(pady=10)
#Label
Label(root, text="Room No").pack()
#Submit button
submit_btn = Button(root, text="Search", command=search, width=25)

submit_btn.pack(pady=10, padx=10, ipadx=100)


root.mainloop()