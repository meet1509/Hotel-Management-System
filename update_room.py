from tkinter import *
from tkinter import messagebox
from rooms import Room
#gui for Upadting rooms
def submit():
    roomNo = int(room_no.get())
    pri = int(price.get())
    category = str(clicked.get())
    room = Room()
    if room.search(roomNo):
        room.update(roomNo, pri, category)
        messagebox.showinfo("Updated", "Room Updated Successfully")
    else:
        messagebox.showinfo("Error", "Room Not Found!")

root = Tk()
root.title('Update Room Details ')
root.geometry("400x600")

clicked = StringVar()
clicked.set("Single")

#Create Entry Widgets
room_no = Entry(root, width=30)
room_no.grid(row=0, column=1, padx=20, pady=(10, 0))
price = Entry(root, width=30)
price.grid(row=1, column=1)
room_type = OptionMenu(root, clicked, "Single", "Double", "Suite", "Presidential Suite")
room_type.grid(row=2, column=1)


# Create Text Box Labels
Label(root, text="Room No.").grid(row=0, column=0, pady=(10, 0))
Label(root, text="Price").grid(row=1, column=0)
Label(root, text="Room Type").grid(row=2, column=0)




# Create Submit Button
submit_btn = Button(root, text="Update Room Details", command=submit, width=25)
submit_btn.grid(row=6, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

root.mainloop()