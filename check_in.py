from tkinter import *
from tkinter import messagebox
from guests import Guest
#gui for check in window
def submit():
    gname = str(name.get())
    ph = int(phone.get())
    room = int(room_no.get())
    guest = Guest()
    if not guest.check_in(gname, ph, room):
        messagebox.showinfo("Room not found", "Room not available")
        return
    messagebox.showinfo("Inserted", "Guest checked in")

root = Tk()
root.title('Check In')
root.geometry("400x600")

clicked = StringVar()
clicked.set("Single")

#create entries
name = Entry(root, width=30)
name.grid(row=0, column=1, padx=20, pady=(10, 0))
phone = Entry(root, width=30)
phone.grid(row=1, column=1)
room_no = Entry(root, width=30)
room_no.grid(row=2, column=1)


# Create Text Box Labels
Label(root, text="Name").grid(row=0, column=0, pady=(10, 0))
Label(root, text="Phone").grid(row=1, column=0)
Label(root, text="Room No.").grid(row=2, column=0)




# Create Submit Button
submit_btn = Button(root, text="Check In", command=submit, width=25)
submit_btn.grid(row=6, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

root.mainloop()