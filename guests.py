import mysql.connector as connector
from rooms import Room

class Guest:
    def __init__(self):
        #constructor to connect the database and create a table guests
        self.con = connector.connect(host='freedb.tech', user='freedbtech_meet', password='Meet@12345', database='freedbtech_hotel')
        query = "create table if not exists guests(user_id int primary key auto_increment, name varchar(200) not null, phone bigint not null, room_no int not null , check_in date not null, check_out date, amount int, foreign key(room_no) references rooms(room_no))"
        cur = self.con.cursor()
        cur.execute(query)


    def check_in(self, name, phone, room_no):
        #function to check in the guests
        room = Room()
        if not room.check_availibility(room_no):
            print("Room Not Available!")
            return False
        query = "insert into guests(name, phone, room_no, check_in) value('{}',{},{}, curdate())".format(name, phone, room_no)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        room.check_in(room_no)
        return True


    def check_out(self, room_no):
        #function to check out the  guests using the room no.
        room = Room()
        if room.check_availibility(room_no) or not room.search(room_no):
            print("Room Already Vacant!")
            return False
    
        days = self.calculate_days(room_no)
        if days == 0:
            amount = room.price(room_no)
        else:
            amount = room.price(room_no) * days
        
        query = "update guests set check_out = curdate(), amount = {} where room_no = {} and check_out is null".format(amount, room_no)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        room.check_out(room_no)
        return True


    def check_out_by_name(self, name):
        #function to check out the  guests using the name
        query = "select room_no from guests where name= '{}' and check_out is null".format(name)
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        if not result:
            print("Guest has not booked any room")
            return False
        for i in result:
            room_no = i[0]
            self.check_out(room_no) 
        return True

    def display(self):
        #function to display all guests
        query = "select * from guests"
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result


    def display_by_name(self, name):
        #search guests by name
        query = "select * from guests where name = '{}'".format(name)
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result


    def display_current_guests_by_room(self, room_no):
        #function to display current guests in a room
        query = "select * from guests where room_no = {} and check_out is null".format(room_no)
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result

    def display_current_guests(self):
        #function to display all current guests
        query = "select * from guests where check_out is null"
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result


    def calculate_days(self, room_no):
        #function to calculate number of days based on check in and check out dates
        query = "select datediff(curdate(), check_in) from guests where room_no = {} and check_out is null".format(room_no)
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        if len(result)>0:
            return result[0][0]
