import sqlite3

con = sqlite3.connect("firstdatabase.db")
cursor = con.cursor()

#cursor.execute(" CREATE TABLE Students (Name VARCHAR(30) , ID VARCHAR(30) PRIMARY KEY ,  Mail VARCHAR(30) , Mobile VARCHAR(20) ")

#cursor.execute("INSERT INTO Students VALUES ('Alaa Abdelwahab','220139484700001','alaa@gmail.com','01000009872') );
#con.commit()

#cursor.execute("INSERT INTO Students VALUES (?,?,?,?)" , ('Alaa Abdelwahab','220139484700001','alaa@gmail.com','01000009872'));
#con.commit()

#cursor.execute("UPDATE Students SET Name='Waleed',ID='2987464645',Mail='waled@gmail.com',Mobile='010092822' WHERE ID='220139484700001' ")
#con.commit()

#cursor.execute("DELETE FROM Students WHERE ID='22013948477560'")
#con.commit()

