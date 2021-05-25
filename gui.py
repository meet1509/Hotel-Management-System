from tkinter import *
from PIL import Image, ImageTk
from subprocess import call

#Homescreen GUI

def add():
    call(["python", "insert_room.py"])
def delete():
    call(["python", "delete.py"])
def update():
    call(["python", "update_room.py"])
def display_all_rooms():
    call(["python", "display_room.py"])
def display_available_rooms():
    call(["python", "display_available_rooms.py"])
def checkin():
    call(["python", "check_in.py"])
def checkout_by_name():
    call(["python", "check_out_by_name.py"])
def checkout_by_no():
    call(["python", "check_out_by_no.py"])
def display_all_guests():
    call(["python", "display_guests.py"])
def display_current_guests():
    call(["python", "display_current_guests.py"])
def display_by_no():
    call(["python", "display_guests_by_number.py"])
def display_by_name():
    call(["python", "display_by_name.py"])

#Create Root
root = Tk()

root.geometry("1000x666")
root.minsize(1000, 666)
root.maxsize(1000, 666)
root.title("Hotel Management System")

#Background Image
image = Image.open("background.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.place(x=0,y=0)

#Heading
Label(text="Hotel Management System", font="comicsansms 16 bold").pack(pady=15)
#Buttons
Button(text="Add Room Details", command=add).pack(pady=10)
Button(text="Delete Room Details", command=delete).pack(pady=10)
Button(text="Update Room Details", command=update).pack(pady=10)
Button(text="Display All Rooms", command=display_all_rooms).pack(pady=10)
Button(text="Display Available Rooms", command=display_available_rooms).pack(pady=10)

Button(text="Check In", command=checkin).pack(pady=10)
Button(text="Check Out By Name", command=checkout_by_name).pack(pady=10)
Button(text="Check Out By Room No", command=checkout_by_no).pack(pady=10)
Button(text="Display All Guests", command=display_all_guests).pack(pady=10)
Button(text="Display Current guests", command=display_current_guests).pack(pady=10)
Button(text="Display Current Guest By Room No", command=display_by_no).pack(pady=10)
Button(text="Search Guests", command=display_by_name).pack(pady=10)
Button(text="Quit", command=quit).pack(pady=10)


root.mainloop()