import mysql.connector as connector
class Room:
    def __init__(self):
        #constructor to connect the database and create a table rooms
        self.con = connector.connect(host='freedb.tech', user='freedbtech_meet', password='Meet@12345', database='freedbtech_hotel')
        query = "create table if not exists rooms(room_no int primary key, price int not null, category varchar(200) not null, available varchar(10) default 'yes' not null)"
        cur = self.con.cursor()
        cur.execute(query)


    def insert(self, room_no, price, roomType):
        #function to insert room in rooms table
        query = "insert into rooms value({},{},'{}','yes')".format(room_no, price, roomType)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()


    def display(self):
        #function to display all rooms
        query = "select * from rooms"
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result


    def display_available_rooms(self):
        #function to display available rooms
        query = "select room_no, price, category from rooms where available = 'yes'"
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result


    def delete(self, room_no):
        #function to delete a room from rooms table
        query = "delete from rooms where room_no = {}".format(room_no)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()


    def update(self, room_no, price, roomType):
        #function to update a room from rooms table
        query = "update rooms set price = {}, category='{}' where room_no={}".format(price, roomType, room_no)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()


    def check_availibility(self, room_no):
        query = "select available from rooms where room_no={}".format(room_no)
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        if len(result)==0:
            return False
        if(result[0][0]=='yes'):
            return True
        else:
            return False


    def check_in(self, room_no):
        query = "update rooms set available='no' where room_no={}".format(room_no)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()


    def check_out(self, room_no):
        query = "update rooms set available='yes' where room_no={}".format(room_no)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()


    def price(self, room_no):
        query = "select price from rooms where room_no = {}".format(room_no)
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result[0][0]

    def search(self, room_no):
        query = "select * from rooms where room_no = {}".format(room_no)
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        if len(result)!=0:
            return True
        else:
            return False
        