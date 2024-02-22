#Get a connection to DB 
import sqlite3


#create database connection
def connect():
    conn=sqlite3.connect('holiday.db')
    cur=conn.cursor()
    return conn, cur

#create table
def createBookingTable():
    conn,cur=connect()
    cur.execute('''CREATE TABLE IF NOT EXISTS holiday(
                no_Passangers NOT NULL,
                itinerary TEXT NOT NULL,
                date_time TEXT NOT NULL,
                price INTEGER NOT NULL,
                total INTEGER NOT NULL)
                ''')
    conn.commit()
    conn.close()

def create_staff_table():
    conn,cur=connect()
    cur.execute('''CREATE TABLE IF NOT EXISTS(
                   staffID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
                   firstname TEXT NOT NULL,
                   lastname TEXT NOT NULL,
                   userbane TEXT NOT NULL,
                   password TEXT NOT NULL)
                   ''')
    conn.commit()
    conn.close()

    #inner booking system
def insert_booking(selected, choosed, choice,  unit_price, total):
    conn,cur=connect()
    a_booking =(selected,choosed, choice, unit_price, total)
    cur.execute('''INSERT INTO holiday(no_passangers, itinerary, date_time, price, total) VALUES(?, ?, ?, ?, ?)''', a_booking)
    conn.commit()
    #conn.close()

def select_all_booking():
    conn,cur= connect()
    alist=cur.execute("SELECT *FROM holiday")
    print("no_passanger\titinerary\tdate_time\t\tprice\ttotal")
    for row in alist:
        print("{}\t\t{}\t{}\t\t\t{}\t{}".format(row[0],row[1],row[2],row[3],row[4]))
    conn.close()

createBookingTable()
select_all_booking()

    
