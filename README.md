# Hotel-Management-System

•	Rooms table maintains the details of the rooms in the hotel like room no., price, category and availibility.
•	Room no. should be unique i.e. it is the primary key.
•	Guests table maintains the details of the guests like user id, name, phone no., room no., check in date, check out date and amount to be paid.
•	 User id should be unique. It is the primary key for the table whose value is given automatically.
•	Room no. is the foreign key which references to room no. in the rooms table.

Assumptions
•	One guest can book multiple rooms.

Relationship

•	Guest-– [ Books ] –- Room 

Getting Started
Install all the packages in the cmd

pip install mysql
pip install mysql-connector-python
pip install Pillow

Open project folder
Run gui.py 
python gui.py


 

