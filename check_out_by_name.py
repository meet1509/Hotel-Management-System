from tkinter import *
from tkinter import messagebox
from guests import Guest
#gui for check out window
def submit():
    gname = str(name.get())
    guest = Guest()
    if not guest.check_out_by_name(gname):        
        messagebox.showinfo("Guest not found", "Guest has not booked any room")
        return
    messagebox.showinfo("Checked Out", "Guest Checked Out Successfully")

root = Tk()
root.title('Check Out')
root.geometry("400x600")

#Create Entry boxes
name = Entry(root, width=30)
name.grid(row=0, column=1, padx=20, pady=(10, 0))


# Create Text Box Labels
Label(root, text="Name").grid(row=0, column=0, pady=(10, 0))




# Create Submit Button
submit_btn = Button(root, text="Check Out", command=submit, width=25)
submit_btn.grid(row=6, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

root.mainloop()