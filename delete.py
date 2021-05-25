from tkinter import *
from rooms import Room
from tkinter import messagebox
#gui for delete room window
def submit():
    roomNo = int(room_no.get())
    room = Room()   
    print("Deleted")
    if room.search(roomNo):
        room.delete(roomNo)
        messagebox.showinfo("Deleted", "Room Deleted Successfully")
    else:
        messagebox.showinfo("Error", "Room Not Found!")
        
    

root = Tk()
root.title('Delete Room Details ')
root.geometry("400x600")

#Create Entry box
room_no = Entry(root, width=30)
room_no.grid(row=0, column=1, padx=20, pady=(10, 0))


# Create Text Box Labels
Label(root, text="Room No.").grid(row=0, column=0, pady=(10, 0))




# Create Submit Button
submit_btn = Button(root, text="Delete Room Details", command=submit, width=25)
submit_btn.grid(row=6, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

root.mainloop()